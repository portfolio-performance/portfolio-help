import re
import os
import sys
import requests
import time
from urllib.parse import urlparse

# Define the directories and their language labels
DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}

# Path to ignore URLs file (adjust path as needed)
IGNORE_URLS_FILE = os.path.join(".github", "ci", "ignore_urls.txt")

# Timeouts for external link check
HTTP_TIMEOUT = 3
MAX_RETRIES = 3
RETRY_DELAY = 3

# Custom headers to simulate a normal web browser request
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


def load_ignore_urls(file_path):
    """Load ignored domains from a text file into a set."""
    ignore_domains = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    domain = get_exact_domain_from_url(line)
                    if domain:
                        ignore_domains.add(domain)
    return ignore_domains


def get_exact_domain_from_url(url):
    """Extract the exact domain from a URL (including subdomains)."""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    return domain


def find_markdown_files(base_dirs):
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


def extract_links_with_line_numbers(md_file):
    links_with_lines = []
    pattern = re.compile(
        r"\[([^\]]+)\]\((https?://[^\s)]+?(?:\([^\s)]+\))*?)\)\s*[.,;!?]*|\[#([^\)]+)\][.,;!?]*",
        re.MULTILINE | re.IGNORECASE,
    )

    with open(md_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            links = pattern.findall(line)
            for link_text, path, anchor in links:
                if path:
                    links_with_lines.append((line_num, link_text, path))
                elif anchor:
                    links_with_lines.append((line_num, link_text, f"#{anchor}"))

    return links_with_lines


def validate_external_link(path, checked_urls, ignore_domains):
    """Validate an external link by checking its availability and content type."""
    domain = get_exact_domain_from_url(path)

    if path in checked_urls:
        return checked_urls[path]

    for attempt in range(MAX_RETRIES):
        try:
            resp = session.head(path, timeout=HTTP_TIMEOUT, allow_redirects=True)

            if resp.status_code in (403, 405):
                print(
                    f"⚠️ Warning: Access to {path} is forbidden (HTTP {resp.status_code}). Retrying with GET..."
                )
                resp = session.get(path, timeout=HTTP_TIMEOUT, allow_redirects=True)

            if resp.status_code == 429:
                print(
                    f"⚠️ Rate-limited (HTTP 429) while accessing {path} --> Retrying after {RETRY_DELAY}s..."
                )
                time.sleep(RETRY_DELAY)
                continue

            if resp.status_code >= 400:
                if domain in ignore_domains:
                    print(
                        f"⚠️ Warning: Link {path} resulted in HTTP {resp.status_code} (ignored domain)."
                    )
                    checked_urls[path] = f"warning: HTTP {resp.status_code}"
                    return f"warning: HTTP {resp.status_code}"
                else:
                    print(f"❌ Error: Link {path} resulted in HTTP {resp.status_code}.")
                    checked_urls[path] = f"HTTP {resp.status_code}"
                    return f"HTTP {resp.status_code}"

            content_type = resp.headers.get("Content-Type", "").lower()

            if "application/json" in content_type:
                print(f"✅ JSON response from {path}, treating it as valid.")
                checked_urls[path] = "OK"
                return "OK"

            if not content_type or "text/html" not in content_type:
                resp = session.get(path, timeout=HTTP_TIMEOUT, allow_redirects=True)
                content_type = resp.headers.get("Content-Type", "").lower()

                if resp.status_code == 429:
                    print(
                        f"⚠️ Rate-limited (HTTP 429) while accessing {path} --> Retrying after {RETRY_DELAY}s..."
                    )
                    time.sleep(RETRY_DELAY)
                    continue

                if resp.status_code >= 400:
                    if domain in ignore_domains:
                        print(
                            f"⚠️ Warning: Link {path} resulted in HTTP {resp.status_code} (ignored domain)."
                        )
                        checked_urls[path] = f"warning: HTTP {resp.status_code}"
                        return f"warning: HTTP {resp.status_code}"
                    else:
                        print(
                            f"❌ Error: Link {path} resulted in HTTP {resp.status_code}."
                        )
                        checked_urls[path] = f"HTTP {resp.status_code}"
                        return f"HTTP {resp.status_code}"

            checked_urls[path] = "OK"
            return "OK"

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

    if domain in ignore_domains:
        print(f"⚠️ Warning: Timeout while accessing {path} (ignored domain).")
        checked_urls[path] = "warning: timeout"
        return "warning: timeout"
    else:
        print(f"❌ Error: Timeout while accessing {path}.")
        checked_urls[path] = "timeout"
        return "timeout"


def validate_links(md_files, ignore_domains):
    issues = []
    checked_urls = {}
    valid_count = 0
    ignored_count = 0
    warning_count = 0
    issue_count = 0
    total_links = 0

    for lang, md_file in md_files:
        links_with_lines = extract_links_with_line_numbers(md_file)
        for line_num, link_text, path in links_with_lines:
            total_links += 1
            if path.startswith("http://") or path.startswith("https://"):
                result = validate_external_link(path, checked_urls, ignore_domains)

                if result == "OK":
                    valid_count += 1
                elif result.startswith("warning"):
                    warning_count += 1
                elif "HTTP" in result or result == "timeout":
                    issue_count += 1
                    issues.append((lang, md_file, line_num, path, result))
            elif path.startswith("#"):
                with open(md_file, "r", encoding="utf-8") as f:
                    file_content = f.read()
                    if path not in file_content:
                        issue_count += 1
                        issues.append(
                            (lang, md_file, line_num, path, "anchor link missing")
                        )
            else:
                abs_path = os.path.normpath(
                    os.path.join(os.path.dirname(md_file), path)
                )
                if not os.path.exists(abs_path):
                    issue_count += 1
                    issues.append(
                        (lang, md_file, line_num, path, "internal link missing")
                    )

    return issues, total_links, valid_count, ignored_count, warning_count, issue_count


if __name__ == "__main__":
    print("🔍 Scanning markdown files for internal and external links...")

    ignore_domains = load_ignore_urls(IGNORE_URLS_FILE)
    if ignore_domains:
        print(
            f"ℹ️ Loaded {len(ignore_domains)} ignored domains from {IGNORE_URLS_FILE}"
        )

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️ No Markdown files found in specified directories.")
        sys.exit(0)

    (
        issues,
        total_links,
        valid_count,
        ignored_count,
        warning_count,
        issue_count,
    ) = validate_links(md_files, ignore_domains)

    print("\n🔎 Validation Results:")

    if issues:
        print("\n❌ Link issues found:")
        for lang, md_file, line_num, link_path, description in issues:
            print(
                f"  [{lang}] In file '{md_file}' at line {line_num}: Link '{link_path}' failed ({description})"
            )
        print(f"\n❌ Validation failed: {len(issues)} issue(s) found.\n")
    else:
        print("\n✅ All internal and external links are valid.")
        print("\n✅ Validation successful: no issues found.\n")

    print("\n📊 Summary:")
    print(f"Total files scanned: {len(md_files)}")
    print(f"Total links checked: {total_links}")
    print(f"Valid links: {valid_count}")
    print(f"Warnings (ignored domains): {warning_count}")
    print(f"Link issues: {issue_count}")

    if issues:
        sys.exit(1)
    else:
        sys.exit(0)
