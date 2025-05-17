import os
import re
import sys
import requests
import time
import random
from collections import defaultdict

# Define the directories and their language labels
DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}

# Path to allowed image domains file
ALLOWED_DOMAINS_FILE = os.path.join(".github", "ci", "allowed_image_domains.txt")


def load_allowed_domains(file_path):
    """Load allowed domains from a text file into a set."""
    disallowed_domains = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    disallowed_domains.add(line.lower())
    return disallowed_domains


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


def validate_images(md_files, allowed_domains):
    """Validate all image references in markdown files."""
    issues = []
    stats = defaultdict(
        lambda: {"files": 0, "images": 0, "allowed": 0, "disallowed": 0}
    )

    for lang, md_file in md_files:
        stats[lang]["files"] += 1

        image_paths = extract_image_paths_with_line_numbers(md_file)
        stats[lang]["images"] += len(image_paths)

        for line_num, path in image_paths:
            if path.startswith("http://") or path.startswith("https://"):
                print(f"🔵  Checking external image {path}")

                if any(domain in path for domain in allowed_domains):
                    print(f"✅  Allowed domain detected {path}")
                    stats[lang]["allowed"] += 1
                    continue

                issues.append(
                    (lang, md_file, line_num, path, "External image link not allowed")
                )
                stats[lang]["disallowed"] += 1
            else:
                # Local images are implicitly allowed
                stats[lang]["allowed"] += 1

    return issues, stats


def print_summary(stats):
    print("\n📊 Breakdown by language:\n")

    total_images = 0
    total_allowed = 0
    total_disallowed = 0

    for lang, data in stats.items():
        images = data["images"]
        allowed = data["allowed"]
        disallowed = data["disallowed"]

        total_images += images
        total_allowed += allowed
        total_disallowed += disallowed

        allowed_pct = (allowed / images * 100) if images else 100.0
        disallowed_pct = (disallowed / images * 100) if images else 0.0

        print(f"[{lang}]")
        print(f"  📄  Files scanned: {data['files']}")
        print(f"  🖼️  Images found: {images}")
        print(f"  ✅  Allowed: {allowed} ({allowed_pct:.1f}%)")
        print(f"  ❌  Disallowed: {disallowed} ({disallowed_pct:.1f}%)\n")

    if total_images > 0:
        total_allowed_pct = total_allowed / total_images * 100
        total_disallowed_pct = total_disallowed / total_images * 100

        print("📈  Overall validation success rate:")
        print(f"  ✅  Allowed: {total_allowed} ({total_allowed_pct:.1f}%)")
        print(f"  ❌  Disallowed: {total_disallowed} ({total_disallowed_pct:.1f}%)\n")


if __name__ == "__main__":
    print(
        "🔍 Scanning markdown files for image references in: "
        + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()])
    )

allowed_domains = load_allowed_domains(ALLOWED_DOMAINS_FILE)
if allowed_domains:
    print(
        f"ℹ️  Loaded {len(allowed_domains)} allowed domains from {ALLOWED_DOMAINS_FILE}"
    )
    print("   Allowed domains:")
    for domain in sorted(allowed_domains):
        print(f"     - {domain}")

md_files = find_markdown_files(DOCS_DIRS)
if not md_files:
    print("⚠️ No Markdown files found in specified directories.")
    sys.exit(0)

issues, stats = validate_images(md_files, allowed_domains)

print_summary(stats)

print("\n🔎 Validation Results:")

if issues:
    print("\n❌  Image issues found:")
    for lang, md_file, line_num, img_path, description in issues:
        print(
            f"  [{lang}] In file '{md_file}' at line {line_num}: Image '{img_path}' failed ({description})"
        )
    print(f"\n❌  Validation failed: {len(issues)} issue(s) found.\n")
    sys.exit(1)
else:
    print("\n✅  Validation successful: no issues found.\n")
    sys.exit(0)
