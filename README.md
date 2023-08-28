# Portfolio Performance Manual

Visit the manual at https://help.portfolio-performance.info

## Setup

The manual is written in Markdown files and generated using [mkdocs](https://www.mkdocs.org) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

The project uses a [multi-language setup](https://github.com/squidfunk/mkdocs-material/discussions/2346):

```
.
├─ config/
│    ├─ en/
│    │  └─ mkdocs.yml
│    └─ de/
│        └─ mkdocs.yml
│
├─ docs/
│    ├─ root/
│    │   ├─ redirects from old URLs ...
│    │   └─ CNAME
│    ├─ en/
│    │   └─ index.md
│    └─ de/
│        └─ index.md
│
└─ overrides/
     ├─ assets/
     │   ├─ images/
     │   │    ├─ favicon.ico
     │   │    └─ logo.svg
     │   │
     │   └─ stylesheets/
     │        └─ extra.css
     │
     └─ partials/
              └─ source.html

```



To run locally, adopt the following instructions to your operating system:

```
mkdocs build -f config/en/mkdocs.yml
mkdocs build -f config/de/mkdocs.yml
cp -R docs/root/* site
cd site
python3 -m http.server
```
