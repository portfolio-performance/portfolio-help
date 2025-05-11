import os
import re
import sys
import yaml
from collections import defaultdict

# Define the directories and their language labels
CONFIG_DIR = {
    "de": os.path.join("config", "de"),
    "en": os.path.join("config", "en"),
}

DOCS_DIRS = {
    "de": os.path.join("docs", "de"),
    "en": os.path.join("docs", "en"),
}

# Function to read the mkdocs.yml configuration and extract the navigation
def read_navigation_config(lang):
    """Reads the mkdocs.yml config for a given language and extracts only the navigation."""
    config_path = os.path.join(CONFIG_DIR[lang], "mkdocs.yml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"⚠️ {config_path} not found.")

    with open(config_path, "r", encoding="utf-8") as f:
        try:
            config = yaml.load(f, Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            print(f"⚠️ Error loading YAML file {config_path}: {e}")
            raise

    # Extract only the 'nav' section
    nav = config.get("nav", [])
    nav_pages = set()

    def extract_nav_links(nav):
        """Extracts links from the navigation structure."""
        for item in nav:
            if isinstance(item, dict):
                for _, sub_nav in item.items():
                    if isinstance(sub_nav, list):
                        for sub_item in sub_nav:
                            if isinstance(sub_item, str):
                                nav_pages.add(sub_item)
                            elif isinstance(sub_item, dict):
                                extract_nav_links(
                                    [sub_item]
                                )  # Recursive call for nested nav items

    extract_nav_links(nav)
    return nav_pages


# Function to find all markdown files
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


# Function to extract front matter from a markdown file
def extract_front_matter(md_file):
    """Extract front matter as a dictionary from a markdown file."""
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
                break  # End of front matter
        if in_front_matter:
            if ":" in line:
                key, value = line.split(":", 1)
                front_matter[key.strip()] = value.strip()

    return front_matter


# Function to detect orphan markdown pages
def detect_orphan_pages(md_files):
    """Detect orphan pages in the markdown files."""
    orphan_pages = []
    stats = defaultdict(lambda: {"files": 0, "orphan_pages": 0})

    # Iterate over each language's files
    for lang, md_file in md_files:
        stats[lang]["files"] += 1
        front_matter = extract_front_matter(md_file)

        # If there is no 'title' in the front matter, treat it as an orphan
        if "title" not in [key.lower() for key in front_matter.keys()]:
            rel_path = os.path.relpath(md_file, start=DOCS_DIRS[lang]).replace(
                "\\", "/"
            )
            orphan_pages.append((lang, rel_path, "Missing front matter 'title' field"))
            stats[lang]["orphan_pages"] += 1

    return orphan_pages, stats


# Function to print the results
def print_summary(stats):
    print("\n📊 Orphan Pages Summary:\n")

    total_files = 0
    total_orphans = 0

    for lang, data in stats.items():
        files = data["files"]
        orphans = data["orphan_pages"]

        total_files += files
        total_orphans += orphans

        orphan_pct = (orphans / files * 100) if files else 0.0

        print(f"[{lang}]")
        print(f"  📄 Files scanned: {files}")
        print(f"  ⚠️ Orphan pages: {orphans} ({orphan_pct:.1f}%)\n")

    if total_files > 0:
        overall_orphan_pct = total_orphans / total_files * 100

        print("📈 Overall orphan page rate:")
        print(
            f"  ⚠️ {total_orphans} orphan pages out of {total_files} files ({overall_orphan_pct:.1f}%)\n"
        )


# Main block to run the validation
if __name__ == "__main__":
    print(
        "🔍 Scanning markdown files for orphan pages in: "
        + ", ".join([f"{lang} ({dir})" for lang, dir in DOCS_DIRS.items()])
    )

    md_files = find_markdown_files(DOCS_DIRS)
    if not md_files:
        print("⚠️ No Markdown files found in specified directories.")
        sys.exit(0)

    orphan_pages, stats = detect_orphan_pages(md_files)

    print_summary(stats)

    print("\n🔎 Validation Results:")

    if orphan_pages:
        print("\n❌ Orphan pages detected:")
        for lang, file_path, description in orphan_pages:
            print(f"  [{lang}] File '{file_path}' ({description})")
        print(f"\n❌ Validation failed: {len(orphan_pages)} orphan page(s) found.\n")
        sys.exit(1)
    else:
        print("\n✅ Validation successful: no orphan pages found.\n")
        sys.exit(0)
