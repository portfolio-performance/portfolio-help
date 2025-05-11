import os
import re
import sys
from collections import defaultdict

# Define the directories and their language labels
DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}

# Supported image extensions
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


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


def extract_image_references(md_file, base_dir):
    """Extract all local image references from a markdown file, resolved relative to base_dir."""
    image_paths = []
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)", re.MULTILINE | re.IGNORECASE)

    md_dir = os.path.dirname(md_file)

    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    matches = pattern.findall(content)
    for path in matches:
        path = path.strip()
        if path.startswith("http://") or path.startswith("https://"):
            continue

        # Resolve relative path based on Markdown file location
        abs_path = os.path.normpath(os.path.join(md_dir, path))

        # Compute relative to base_dir (e.g., docs/de/)
        rel_path = os.path.relpath(abs_path, start=base_dir)
        normalized_ref = rel_path.replace("\\", "/")

        image_paths.append(normalized_ref)

    return image_paths


def find_local_image_files(base_dir):
    """Find all image files in any 'images' folder under base_dir (absolute paths)."""
    image_files = set()

    for root, dirs, files in os.walk(base_dir):
        if os.path.basename(root).lower() == "images":
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in IMAGE_EXTENSIONS:
                    rel_path = os.path.relpath(os.path.join(root, file), start=base_dir)
                    image_files.add(rel_path.replace("\\", "/"))
    return image_files


def validate_unused_images(md_files):
    """Validate all local image files to find unused ones."""
    issues = []
    stats = defaultdict(
        lambda: {"files": 0, "images_found": 0, "images_referenced": 0, "unused": 0}
    )

    references_per_lang = defaultdict(set)

    # Collect all references from markdown files (absolute paths)
    for lang, md_file in md_files:
        stats[lang]["files"] += 1
        refs = extract_image_references(md_file, base_dir=DOCS_DIRS[lang])
        references_per_lang[lang].update(refs)

    # Find all actual image files and compare (absolute paths)
    for lang, base_dir in DOCS_DIRS.items():
        if not os.path.exists(base_dir):
            continue

        all_images = find_local_image_files(base_dir)
        stats[lang]["images_found"] = len(all_images)

        referenced = references_per_lang[lang]
        used_images = all_images & referenced
        stats[lang]["images_referenced"] = len(used_images)

        unused_images = all_images - referenced
        stats[lang]["unused"] = len(unused_images)

        for img_abs in sorted(unused_images):
            rel_img = os.path.relpath(img_abs, start=base_dir).replace("\\", "/")
            issues.append(
                (lang, rel_img, "Image file not referenced in any markdown file")
            )

    return issues, stats


def print_summary(stats):
    print("\n📊 Breakdown by language:\n")

    total_images = 0
    total_referenced = 0
    total_unused = 0

    for lang, data in stats.items():
        images = data["images_found"]
        referenced = data["images_referenced"]
        unused = data["unused"]

        total_images += images
        total_referenced += referenced
        total_unused += unused

        referenced_pct = (referenced / images * 100) if images else 0.0
        unused_pct = (unused / images * 100) if images else 0.0

        print(f"[{lang}]")
        print(f"  📄  Files scanned: {data['files']}")
        print(f"  🖼️  Images found: {images}")
        print(f"  ✅  Referenced: {referenced} ({referenced_pct:.1f}%)")
        print(f"  ❌  Unused: {unused} ({unused_pct:.1f}%)\n")

    if total_images > 0:
        total_referenced_pct = total_referenced / total_images * 100
        total_unused_pct = total_unused / total_images * 100

        print("📈  Overall image usage rate:")
        print(f"  ✅  Referenced: {total_referenced} ({total_referenced_pct:.1f}%)")
        print(f"  ❌  Unused: {total_unused} ({total_unused_pct:.1f}%)\n")

if __name__ == "__main__":
    print(
        "🔍 Scanning markdown files for unused image files in: "
        + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()])
    )

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️ No Markdown files found in specified directories.")
        sys.exit(0)

    issues, stats = validate_unused_images(md_files)

    print_summary(stats)

    print("\n🔎 Validation Results:")

    if issues:
        print("\n❌ Unused images found:")
        for lang, img_path, description in issues:
            print(f"  [{lang}] Unused image '{img_path}' ({description})")
    else:
        print("\n✅  Validation successful: no unused images found.\n")

    # This check is only informational and does not fail the build (for now)
    sys.exit(0)