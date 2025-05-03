import re
import os
import sys
import requests
import time
import json

# Define the directories and their language labels
DOCS_DIRS = {
    'de': os.path.join('docs', 'de'),
    'en': os.path.join('docs', 'en'),
}

# Path to ignore URLs file (adjust path as needed)
IGNORE_URLS_FILE = os.path.join('.github', 'ci', 'ignore_urls.txt')

# Timeouts for external link check (in seconds)
HTTP_TIMEOUT = 3  # Increased timeout

# Retry settings
MAX_RETRIES = 3  # Increased retries
RETRY_DELAY = 3  # seconds

# Custom headers to simulate a normal web browser request (added more headers to bypass Cloudflare)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',  # Do Not Track header
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.google.com/',  # Adding a generic referer
    'X-Requested-With': 'XMLHttpRequest',  # Common header for AJAX requests
    'TE': 'Trailers',  # To simulate a proper HTTP request
}

# List of URLs to ignore during validation.
# These URLs are intentionally excluded because they are known to:
# - block automated requests (e.g., strict firewalls, captchas)
# - be dynamically generated or frequently rate-limited
# - consistently cause false positives in link checking
# The ignore list is maintained in a separate file (ignore_urls.txt) for easy updates.
def load_ignore_urls(file_path):
    """Load ignored URLs from a text file into a set."""
    ignore_urls = set()
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    ignore_urls.add(line)
    return ignore_urls

def find_markdown_files(base_dirs):
    md_files = []
    for lang, base_dir in base_dirs.items():
        if not os.path.exists(base_dir):
            print(f"⚠️ Warning: Directory '{base_dir}' [{lang}] does not exist. Skipping.")
            continue
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".md"):
                    md_files.append((lang, os.path.join(root, file)))
    return md_files

def extract_links_with_line_numbers(md_file):
    links_with_lines = []
    pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+?(?:\([^\s)]+\))*?)\)\s*[.,;!?]*|\[#([^\)]+)\][.,;!?]*', re.MULTILINE | re.IGNORECASE)
    
    with open(md_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            links = pattern.findall(line)
            for link_text, path, anchor in links:
                if path:
                    # External link
                    links_with_lines.append((line_num, link_text, path))
                elif anchor:
                    # Internal anchor link
                    links_with_lines.append((line_num, link_text, f'#{anchor}'))
    
    return links_with_lines

def validate_external_link(path, checked_urls):
    session = requests.Session()  # Create a session to reuse headers and connections
    session.headers.update(HEADERS)  # Apply the custom headers to the session

    # Check if the link has already been validated (cached)
    if path in checked_urls:
        return checked_urls[path]

    for attempt in range(MAX_RETRIES):
        try:
            # Use GET request directly (HEAD requests are often blocked by some sites)
            resp = session.get(path, timeout=HTTP_TIMEOUT, allow_redirects=True, stream=True)

            # Check the Content-Type header
            content_type = resp.headers.get('Content-Type', '').lower()

            # If Content-Type is application/json, the link is considered valid
            if 'application/json' in content_type:
                checked_urls[path] = (None, resp.url)  # Cache the result
                return (None, resp.url)  # Valid link, no error

            # Handle other status codes (without retry logic)
            if resp.status_code == 429:
                print(f"⚠️ Rate-limited (HTTP 429) while accessing {path} --> Retrying after {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)  # Wait before retrying
                continue
            elif resp.status_code == 403:
                print(f"⚠️ Access forbidden (HTTP 403) for {path}")
                checked_urls[path] = ('HTTP 403', None)  # Cache the result
                return ('HTTP 403', None)
            elif resp.status_code == 404:
                print(f"❌ Error while accessing {path} --> HTTP 404 (Not Found)")
                checked_urls[path] = ('HTTP 404', None)  # Cache the result
                return ('HTTP 404', None)
            elif resp.status_code >= 400:
                print(f"⚠️ Error while accessing {path} --> HTTP {resp.status_code}")
                checked_urls[path] = (f"HTTP {resp.status_code}", None)  # Cache the result
                return (f"HTTP {resp.status_code}", None)

            # If we got a valid response, return the URL without issues
            checked_urls[path] = (None, resp.url)  # Cache the result
            return (None, resp.url)

        except requests.exceptions.Timeout:
            print(f"⚠️ Timeout while accessing {path} --> Retrying ({attempt + 1}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error while accessing {path} --> {str(e)} --> Retrying ({attempt + 1}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)

    checked_urls[path] = ('timeout', None)  # Cache the result
    return ('timeout', None)

def validate_links(md_files, ignore_urls):
    issues = []
    checked_urls = {}  # Cache to store already validated external links

    for lang, md_file in md_files:
        links_with_lines = extract_links_with_line_numbers(md_file)
        for line_num, link_text, path in links_with_lines:
            if path.startswith("http://") or path.startswith("https://"):
                if path in ignore_urls:
                    print(f"🔵 Skipping validation for {path} (ignored)")
                    continue

                if path in checked_urls:
                    # Reuse cached validation result
                    error_desc, _ = checked_urls[path]
                else:
                    # Validate external link and store result in cache
                    error_desc, _ = validate_external_link(path, checked_urls)

                if error_desc:
                    description = error_desc if error_desc != 'timeout' else 'timeout'
                    issues.append((lang, md_file, line_num, path, description))

            elif path.startswith("#"):
                with open(md_file, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    if path not in file_content:
                        issues.append((lang, md_file, line_num, path, 'anchor link missing'))
            else:
                abs_path = os.path.normpath(os.path.join(os.path.dirname(md_file), path))
                if not os.path.exists(abs_path):
                    description = 'internal link missing'
                    issues.append((lang, md_file, line_num, path, description))

    return issues

if __name__ == "__main__":
    print("🔍 Scanning markdown files for internal and external links in: " + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()]))

    ignore_urls = load_ignore_urls(IGNORE_URLS_FILE)
    if ignore_urls:
        print(f"ℹ️ Loaded {len(ignore_urls)} ignored URLs from {IGNORE_URLS_FILE}")

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️ No Markdown files found in specified directories.")
        sys.exit(0)

    issues = validate_links(md_files, ignore_urls)

    print("\n🔎 Validation Results:")

    if issues:
        print("\n❌ Link issues found:")
        for lang, md_file, line_num, link_path, description in issues:
            print(f"  [{lang}] In file '{md_file}' at line {line_num}: Link '{link_path}' failed ({description})")
        print(f"\n❌ Validation failed: {len(issues)} issue(s) found.\n")
        sys.exit(1)
    else:
        print("\n✅ All internal and external links are valid.")
        print("\n✅ Validation successful: no issues found.\n")
        sys.exit(0)
