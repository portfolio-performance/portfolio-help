#!/bin/bash

# Change directory to config/en
cd config/en || { echo "Directory config/en not found"; exit 1; }

# Activate the pipx environment for mkdocs (assuming it's named mkdocs)
mkdocs serve
