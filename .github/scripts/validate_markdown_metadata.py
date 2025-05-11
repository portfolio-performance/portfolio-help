import os
import re
import sys
from collections import defaultdict

# Define the directories and their language labels
DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}

# Required Markdown meta-data fields (case-insensitive)
REQUIRED_FIELDS = {"title"}


def find_markdown_files(base_dirs):
    """Recursively find all markdown files in given directories."""
    md_files = []
    for lang, base_dir in base_dirs.items():
        if not os.path.exists(base_dir):
            print(
                f"⚠️  Warning: Directory '{base_dir}' [{lang}] does not exist. Skipping."
            )
            continue
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".md"):
                    md_files.append((lang, os.path.join(root, file)))
    return md_files


def extract_front_matter(md_file):
    """Extract Markdown meta-data matter as a dictionary from a markdown file."""
    front_matter = {}
    in_front_matter = False

    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line == "---":
            if not in_front_matter:
                in_front_matter = True
                continue
            else:
                break  # End of meta-data
        if in_front_matter:
            if ":" in line:
                key, value = line.split(":", 1)
                front_matter[key.strip()] = value.strip()

    return front_matter


def validate_front_matter(md_files):
    """Validate meta-data of Markdown files."""
    issues = []
    stats = defaultdict(lambda: {"files": 0, "missing_fields": 0})

    required_lower = {field.lower() for field in REQUIRED_FIELDS}

    for lang, md_file in md_files:
        stats[lang]["files"] += 1
        front_matter = extract_front_matter(md_file)

        # Normalize keys to lowercase
        front_matter_lower = {k.lower(): v for k, v in front_matter.items()}

        missing = required_lower - front_matter_lower.keys()
        if missing:
            rel_path = os.path.relpath(md_file, start=DOCS_DIRS[lang]).replace(
                "\\", "/"
            )
            # Report missing fields using original casing from REQUIRED_FIELDS
            missing_fields_display = sorted(
                {field for field in REQUIRED_FIELDS if field.lower() in missing}
            )
            issues.append(
                (
                    lang,
                    rel_path,
                    f"Missing required fields: {', '.join(missing_fields_display)}",
                )
            )
            stats[lang]["missing_fields"] += len(missing)

    return issues, stats


def print_summary(stats):
    print("\n📊 Front Matter Validation Summary:\n")

    total_files = 0
    total_missing = 0

    for lang, data in stats.items():
        files = data["files"]
        missing = data["missing_fields"]

        total_files += files
        total_missing += missing

        missing_pct = (missing / files * 100) if files else 0.0

        print(f"[{lang}]")
        print(f"  📄  Files scanned: {files}")
        if missing > 0:
            print(f"  ⚠️  Files with missing fields: {missing} ({missing_pct:.1f}%)")

    if total_files > 0:
        overall_missing_pct = total_missing / total_files * 100

        print("\n📈  Overall Markdown meta-data matter completeness rate:")
        if total_missing > 0:
            print(
                f"  ⚠️  Missing fields in {total_missing} of {total_files} files ({overall_missing_pct:.1f}%)"
            )
        else:
            print(
                f"  ✅  All {total_files} files have complete Markdown meta-data"
            )

if __name__ == "__main__":
    print(
        "🔍 Scanning markdown files for missing required Markdown meta-data fields in: "
        + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()])
    )

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️  No Markdown files found in specified directories.")
        sys.exit(0)

    issues, stats = validate_front_matter(md_files)

    print_summary(stats)

    print("\n\n🔎 Validation Results:")

    if issues:
        print("\n❌  Missing Markdown meta-data detected:")
        for lang, file_path, description in issues:
            print(f"  [{lang}] File '{file_path}' ({description})")
        print(
            f"\n❌  Validation failed: {len(issues)} file(s) with missing in the Markdown meta-data.\n"
        )
    else:
        print("\n✅  Validation successful: all required Markdown meta-data fields are present.\n")

    sys.exit(0)