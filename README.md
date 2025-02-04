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

## Contributing

Contributing to a Github project such as the PortfolioPerformance Help manual may seem intimidating at first due to the number of steps involved. However, once you've completed the process, you'll find it to be straightforward and simple thereafter.

We'll start by providing a broad overview. The following 5 steps are needed.

1. **Forking**: Forking creates a personal (independent) copy of someone else's project. This allows you to freely experiment with changes without affecting the original project.

2. **Cloning**: Cloning is the process of downloading a copy of the repository from GitHub to your local machine. This allows you to work on the project locally, using your preferred tools and editors.

3. **Committing**: Committing is the process of saving your changes locally. In Git, every time after you made changes, you need to commit those changes, which saves a snapshot of your work at that point in time.

4. **Pushing**: Pushing is the process of uploading your local repository, including all of your commits, to your GitHub account. This updates your forked repository on GitHub with your latest changes.

5. **Creating a Pull Request**: Once you've pushed your changes to GitHub, the next step is to notify the original repository maintainers of your changes. This is done by creating a pull request. In the pull request, you propose your changes and request that the original repository maintainers pull your changes into their repository.


The following step-by-step guide assumes that you are a novice and do not have a GitHub account.

1. **Create a GitHub Account (if you don't already have one)**
    - Go to [GitHub](https://github.com/) and click on `Sign up`.
    - Fill in your details and follow the instructions to create your account.

2. **Fork the Portfolio Help Repository**
    - Go to the [portfolio-help repository](https://github.com/portfolio-performance/portfolio-help).
    - Click on the `Fork` button at the top right corner. This creates a copy of the repository in your account.

3. **Install Git Locally**
    - Download and install Git from the [official website](https://git-scm.com/downloads).
    - Open your terminal (Command Prompt on Windows, Terminal app on macOS) and verify the installation by typing `git --version`. You should see a version number which means Git is installed correctly.

4. **Clone the Portfolio Help Repository Locally**
    - On your GitHub page, go to your forked repository.
    - Click on the `Code` button and copy the URL.
    - Open your terminal, navigate to the directory where you want to clone the repository using `cd <directory>`.
    - Clone the repository by typing `git clone <URL>`.

5. **Make Changes**
    - The following instructions assume that you are working with a simple editor e.g. Notepad. If you are using a tool such as Visual Studio Code, things are a lot easier. 
    - Navigate into the cloned repository directory (`cd portfolio-help`).
    - Create a new branch for your changes (`git checkout -b <branch-name>`).
    - Make your changes in the repository files.

6. **Commit and Push Your Changes**
    - Stage your changes (`git add .`).
    - Commit your changes (`git commit -m "<commit-message>"`).
    - Push your changes to your GitHub (`git push origin <branch-name>`).

7. **Create a Pull Request**
    - Go to your GitHub page and navigate to your forked repository.
    - Click on `Pull request` and then `New pull request`.
    - Select your branch from the dropdown menu and click `Create pull request`.
    - Fill in the details of your changes and then click `Create pull request`.

8. **Wait for Review**
    - Once you've submitted your pull request, wait for the repository maintainers to review your changes. They may ask for some modifications or improvements before merging your changes.

There are lots of tutorials on YouTube: search for github + one of the previous keywords "fork", "clone", "commit", ...

