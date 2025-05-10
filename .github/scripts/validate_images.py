import os
import re
import sys
import requests
import time
import random

# Define the directories and their language labels
DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}

# Path to disallowed domains file
DISALLOWED_DOMAINS_FILE = os.path.join(".github", "ci", "disallowed_image_domains.txt")

# Timeouts for external image check
HTTP_TIMEOUT = 3
MAX_RETRIES = 3
RETRY_DELAY = 3

# Custom headers to simulate a normal web browser request (added more headers to bypass restrictions like Cloudflare)
SESSION_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.50 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Cache-Control": "max-age=0",
    "X-Requested-With": "XMLHttpRequest",
    "TE": "Trailers",
    "Referer": "https://www.portfolio-performance.info/",
    "Origin": "https://www.portfolio-performance.info",
}

# Reusable session for all requests
session = requests.Session()
session.headers.update(SESSION_HEADERS)


def load_disallowed_domains(file_path):
    """Load disallowed domains from a text file into a set."""
    disallowed_domains = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    disallowed_domains.add(line.lower())
    return disallowed_domains


def is_disallowed_url(path, disallowed_domains):
    """Return True if the URL contains any disallowed domain."""
    return any(domain in path.lower() for domain in disallowed_domains)


def find_markdown_files(base_dirs):
    """Recursively find all markdown files in given directories."""
    md_files = []
    for lang, base_dir in base_dirs.items():
        if not os.path.exists(base_dir):
            print(
                f"⚠️ Warning: Directory '{base_dir}' [{lang}] does not exist. Skipping."
            )
            continue
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".md"):
                    md_files.append((lang, os.path.join(root, file)))
    return md_files


def extract_image_paths_with_line_numbers(md_file):
    """Extract all image references from a markdown file with their line numbers."""
    image_paths = []
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)", re.MULTILINE | re.IGNORECASE)

    with open(md_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            matches = pattern.findall(line)
            for path in matches:
                image_paths.append((line_num, path.strip()))
    return image_paths


def validate_external_image(path, checked_urls):
    """Validate an external image URL by checking availability and content type."""

    if path in checked_urls:
        return checked_urls[path]

    for attempt in range(MAX_RETRIES):
        try:
            resp = session.head(path, timeout=HTTP_TIMEOUT, allow_redirects=True)

            if resp.status_code in (403, 405):
                print(
                    f"⚠️ Warning: Access denied (HTTP {resp.status_code}) while accessing {path}."
                )
                checked_urls[path] = f"HTTP {resp.status_code}"
                return f"HTTP {resp.status_code}"

            if "image/" not in resp.headers.get("Content-Type", "").lower():
                # Fallback to GET immediately if HEAD is blocked OR doesn't return content type
                resp = session.get(path, timeout=HTTP_TIMEOUT, allow_redirects=True)

            if resp.status_code == 429:
                print(
                    f"⚠️ Warning: Rate-limited (HTTP 429) while accessing {path} --> Retrying after {RETRY_DELAY}s..."
                )
                time.sleep(RETRY_DELAY)
                continue
            elif resp.status_code == 404:
                print(f"❌ Error: HTTP 404 (Not Found) while accessing {path}.")
                checked_urls[path] = "HTTP 404"
                return "HTTP 404"
            elif resp.status_code >= 400:
                print(f"⚠️ Error: HTTP {resp.status_code} while accessing {path}.")
                checked_urls[path] = f"HTTP {resp.status_code}"
                return f"HTTP {resp.status_code}"

            content_type = resp.headers.get("Content-Type", "").lower()
            if not content_type.startswith("image/"):
                checked_urls[path] = f"unexpected content type ({content_type})"
                return f"unexpected content type ({content_type})"

            checked_urls[path] = "OK"
            return None

        except requests.exceptions.Timeout:
            print(
                f"⚠️ Timeout while accessing {path} --> Retrying ({attempt + 1}/{MAX_RETRIES})..."
            )
            time.sleep(RETRY_DELAY)
        except requests.exceptions.RequestException as e:
            print(
                f"⚠️ Error while accessing {path} --> {str(e)} --> Retrying ({attempt + 1}/{MAX_RETRIES})..."
            )
            time.sleep(RETRY_DELAY)

    checked_urls[path] = "timeout"
    return "timeout"


def validate_images(md_files, disallowed_domains):
    """Validate all image references in markdown files."""
    issues = []
    checked_urls = {}

    for lang, md_file in md_files:
        image_paths = extract_image_paths_with_line_numbers(md_file)
        for line_num, path in image_paths:
            if path.startswith("http://") or path.startswith("https://"):
                print(f"🔵 Checking external image {path}")

                if is_disallowed_url(path, disallowed_domains):
                    description = "disallowed domain"
                    issues.append((lang, md_file, line_num, path, description))
                    print(f"❌ Disallowed domain detected {path}")
                    continue

                error_desc = validate_external_image(path, checked_urls)

                if error_desc:
                    description = error_desc if error_desc != "timeout" else "timeout"
                    issues.append((lang, md_file, line_num, path, description))

            else:
                abs_path = os.path.normpath(
                    os.path.join(os.path.dirname(md_file), path)
                )
                if not os.path.exists(abs_path):
                    description = "local image missing"
                    issues.append((lang, md_file, line_num, path, description))

    return issues


if __name__ == "__main__":
    print(
        "🔍 Scanning markdown files for image references in: "
        + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()])
    )

    disallowed_domains = load_disallowed_domains(DISALLOWED_DOMAINS_FILE)
    if disallowed_domains:
        print(
            f"ℹ️ Loaded {len(disallowed_domains)} disallowed domains from {DISALLOWED_DOMAINS_FILE}"
        )

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️ No Markdown files found in specified directories.")
        sys.exit(0)

    issues = validate_images(md_files, disallowed_domains)

    print("\n🔎 Validation Results:")

    if issues:
        print("\n❌ Image issues found:")
        for lang, md_file, line_num, img_path, description in issues:
            print(
                f"  [{lang}] In file '{md_file}' at line {line_num}: Image '{img_path}' failed ({description})"
            )
        print(f"\n❌ Validation failed: {len(issues)} issue(s) found.\n")
        sys.exit(1)
    else:
        print("\n✅ All image references (local & external) are valid.")
        print("\n✅ Validation successful: no issues found.\n")
        sys.exit(0)
