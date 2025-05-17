import os
import sys
from collections import defaultdict

# Define the directories and their language labels
DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}


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


def is_file_effectively_empty(md_file):
    """Check if a markdown file contains no meaningful content besides optional front matter."""
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    content_lines = []
    in_front_matter = False
    front_matter_handled = False

    for line in lines:
        stripped = line.strip()
        if not front_matter_handled:
            if stripped == "---":
                if not in_front_matter:
                    in_front_matter = True
                    continue
                else:
                    in_front_matter = False
                    front_matter_handled = True
                    continue
        if in_front_matter:
            continue
        content_lines.append(stripped)

    # Remove empty lines
    meaningful_content = [line for line in content_lines if line]

    return len(meaningful_content) == 0


def validate_empty_markdown_files(md_files):
    """Identify effectively empty markdown files (only front matter or nothing)."""
    issues = []
    stats = defaultdict(lambda: {"files": 0, "empty": 0})

    for lang, md_file in md_files:
        stats[lang]["files"] += 1
        if is_file_effectively_empty(md_file):
            rel_path = os.path.relpath(md_file, start=DOCS_DIRS[lang]).replace(
                "\\", "/"
            )
            issues.append(
                (lang, rel_path, "Markdown file is empty or contains only front matter")
            )
            stats[lang]["empty"] += 1

    return issues, stats


def print_summary(stats):
    print("\n📊 Breakdown by language:\n")

    total_files = 0
    total_empty = 0

    for lang, data in stats.items():
        files = data["files"]
        empty = data["empty"]

        total_files += files
        total_empty += empty

        empty_pct = (empty / files * 100) if files else 0.0

        print(f"[{lang}]")
        print(f"  📄 Files scanned: {files}")
        print(f"  ❌ Empty files: {empty} ({empty_pct:.1f}%)\n")

    if total_files > 0:
        total_empty_pct = total_empty / total_files * 100

        print("📈 Overall file emptiness rate:")
        print(f"  ❌ Empty files: {total_empty} ({total_empty_pct:.1f}%)\n")


if __name__ == "__main__":
    print(
        "🔍 Scanning markdown files for empty or front matter-only files in: "
        + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()])
    )

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️ No Markdown files found in specified directories.")
        sys.exit(0)

    issues, stats = validate_empty_markdown_files(md_files)

    print_summary(stats)

    print("\n🔎 Validation Results:")

    if issues:
        print("\n❌ Empty markdown files found:")
        for lang, md_path, description in issues:
            print(f"  [{lang}] Empty file '{md_path}' ({description})")
        print(f"\n❌ Validation failed: {len(issues)} empty markdown file(s) found.\n")
        sys.exit(1)
    else:
        print("\n✅ Validation successful: no empty markdown files found.\n")
        sys.exit(0)
