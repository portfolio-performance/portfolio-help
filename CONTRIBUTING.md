# Contributing to Portfolio Performance Manual

## Contents


  - [Writing setup](#writing-setup)
    - [Source files of the Portfolio Performance Manual](#source-files-of-the-portfolio-performance-manual)
    - [MkDocs & Material for MkDocs](#mkdocs--material-for-mkdocs)
  - [Navigation](#navigation)
  - [Style guide](#style-guide)
    - [Figure captions](#figure-captions)

## Writing setup

The Portfolio Performance Manual is written in Markdown language and build with the open-source MkDocs static site generator and the Material for MkDocs framework.

### Source files of the Portfolio Performance Manual

The Markdown source files of the manual can be retrieved from [https://github.com/portfolio-performance/portfolio-help](https://github.com/portfolio-performance/portfolio-help). In order to contribute to the manual, you need to fork the repository and clone this repo locally; see [Github docs](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) for a detailed workflow. The directory structure of the manual looks like:

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
│    │   ├─ concepts
     │   │    ├─ account.md
     │   │    ├─ xxx.md     
│    └─ de/
│        └─ index.md
│
└─ overrides/
     ├─ assets/
     │   ├─ images/
     │   │    ├─ favicon.ico
     │   │    └─ logo.svg
     │   ├─ javascripts/
     │   │    └─ katex.js
     │   └─ stylesheets/
     │        └─ extra.css
     └─ partials/
              └─ source.html

```

At present, the manual is available in two languages: English (en) and German (de). All documentation pages should be stored within these directories; including images.


Use your favorite (Markdown) text editor to make corrections to the (local) source files. Upon finishing, create a Pull Request to the maintainer of the PP manual. If accepted, your changes will be visible within minutes. 

### MkDocs & Material for MkDocs

Only if you need to view your changes locally and within the integrated Materials framework, you need to install both Python modules: [MkDocs installation](https://www.mkdocs.org/user-guide/installation/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/).

Minor changes can be easily previewed within your Markdown editor.

## Navigation
The manual is organized into three levels of navigation: the top menu, left sidebar, and right sidebar.

- The top menu displays the primary sections of the manual, such as `About`, `Getting started`, and `Basic concepts` 

   Figure: Top-level menu. {pp-figure}

   ![](overrides/assets/images/top-level-menu.png)


- The left sidebar provides the structure of the selected top menu item, including all chapters and pages within it, e.g. `Getting started`.

- The right sidebar displays an overview of all header topics on the currently viewed page, e.g. `Create portfolio`.

The navigation structure is described in the mkdocs.yml files; one for each language.

```yaml
nav:
  - About this manual: index.md
  - Getting started:
      - Getting started: getting-started/index.md
      - Installation: getting-started/installation.md
      - ...
```

## Style guide

A documentation style guide is a set of standards for document writing, ensuring consistency in style and formatting. Numerous comprehensive style guides are available. Below, we describe only a few style rules that are specific to the PP manual. For all other situations, we recommend consulting the [Microsoft Writing Style Guide]((https://learn.microsoft.com/en-us/style-guide/welcome/)), which covers topics such as capitalization of words, numbers, and the choice between active and passive voice.

### Figure captions

All figures in the manual should be accompanied by a numbered figure caption, allowing for easy reference in the text, such as "see Figure 1." The manual utilizes the [MkDocs Caption plugin](https://pypi.org/project/mkdocs-caption/) to automate this process.

To include a figure (or table) with a caption, insert the following code.

```
Figure: Example of Deposit Accounts. {class="pp-figure"}

![](../images/mnu-transaction-buy.png)
```
The figure caption is written after `Figure:`. You can add a class to the figure with {myclass}. The reference to the figure is plain Markdown syntax.

All images are stored in a folder named `images` at the language level, which means they are placed within the `en` or `de` folder at the top level. The naming convention follows Kebab case, where spaces are replaced with hyphens. Additionally, the image names provide an indication of their source or origin. For instance, "mnu-transaction-buy.png" is a screenshot, produces from the top-level menu `Transaction > Buy`. 
