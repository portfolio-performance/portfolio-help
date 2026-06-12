#!/bin/bash

# Activate venv if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "No .venv found. Create it with: python3 -m venv .venv"
    exit 1
fi

# Move into the docs folder
cd config/en || { echo "Directory config/en not found"; exit 1; }

# Check if mkdocs is installed
if ! command -v mkdocs >/dev/null 2>&1; then
    echo "mkdocs not found in the virtual environment."
    echo "Install it with: pip install mkdocs mkdocs-material"
    exit 1
fi

mkdocs serve --dirtyreload --livereload -a localhost:8005
