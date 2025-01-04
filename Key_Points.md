# KEY POINTS
* **Linus Torvalds** is the founder of Git. Originally, Git was an acronym for **"Global Information Tracker"**, but nowadays, it's mostly just a name.

### Git:
* A Command-Line Interface tool, used as a Version Control System.

* Tracks and records changes in source code, including **date, time, author, and commit history**.
* Helps developers collaborate and manage code efficiently.
* **Commit**: A snapshot of changes in the repository. Each commit is identified by a unique SHA hash.
* **Merge**: Integrates changes from one branch into another; usually from a feature branch to main or dev.
* **Rebase**: Re-applies commits on top of another base commit to rewrite history for cleaner linear logs.
* **Pull Requests**: A feature of GitHub for proposing changes, reviewing code, and merging updates from one branch to another.
* **Conflict Resolution**: Occurs when multiple changes are made to the same file. Git requires manual resolution before merging.

### GitHub:
* A web-based platform for hosting Git repositories.

* Includes all Git features and adds more features such as issue tracking, pull requests, and CI/CD pipelines through **GitHub Actions**.
* Lets you store, manage, and collaborate on code repositories.

### BitBucket:
* A Source Code Management platform similar to GitHub, but it integrates very well with other Atlassian tools like **JIRA** for issue and ticket management.

## KEY DIFFERENCES
### File System vs. Version Control System (VCS):
* **File System**: It cannot recover or rollback deleted files. Doesn't track and version files.

* **VCS**: Tracks changes to files, allowing rollback and recovery. Keeps a version history of each file.

### Main Branch vs. Master Branch:
* **Main Branch**: Default branch name when a repository is created on GitHub (as of 2020, GitHub switched to "main" for inclusivity).

* **Master Branch**: Default branch name for older repositories and local Git repositories unless renamed.

### GitHub Fork vs. Clone:
* **Fork**: Creates a copy of a GitHub repository under your own account for independent development. The original repository is not modified.

* **Clone**: Makes a local copy of a GitHub repository onto your system to work offline.

## Branches in Git
Branches represent isolated copies of the code for specific purposes, thus allowing parallel development.

* **Main/Master Branch**: The production-ready or mainline code.

* **Staging Branch**: Used for testing changes before moving to production.
* **Development (Dev) Branch**: Used for ongoing development.
* **Feature Branch**: Used for individual tasks or features. These are merged into the Dev branch when finished.

## Key Terms
### HEAD
HEAD Refers to the most recent commit on your current branch. It's the pointer to the current state of the repository.

### Git Fetch vs. Git Pull
* **Fetch**: Downloads all changes and branch information from the remote repository without applying them to the local branch.

* **Pull**: Combines `fetch` and `merge`, applying the downloaded changes to the local branch.

## GitHub Actions
GitHub Actions is a CI/CD tool that comes built-in with GitHub. It automates software workflows, such as:

**Scanning → Building → Testing → Deploying** code.