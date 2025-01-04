# Concepts:

## What is Git?
Git is a distributed version control system used to track changes in source code during software development. It helps teams collaborate by managing changes, allowing multiple developers to work on the same project simultaneously.

## What is GitHub?
GitHub is a web-based platform built on top of Git that enables developers to host, manage, and collaborate on their Git repositories. It also includes additional features like issue tracking, pull requests, and GitHub Actions for automation.

## How does Git differ from GitHub?
* **Git**: A version control tool that runs locally to track code changes.
* **GitHub**: A cloud-based platform for hosting Git repositories and enabling team collaboration.

## What is a Version Control System?
A Version Control System (VCS) is a tool that helps track changes to files over time, enabling collaboration and rollback to previous versions if needed. Examples include Git, Subversion, and Mercurial.

## What are the things recorded by Git & GitHub?
* **Git**: Tracks changes to files, commit history, and branches in the repository.

* **GitHub**: Stores repository files, tracks commit history, and maintains issues, pull requests, and collaboration activities.

## What is GitLab?
GitLab is an open-source DevOps platform similar to GitHub, offering Git repository hosting, CI/CD pipelines, issue tracking, and more. It's often used for on-premises setups.

## How does File System differ from Version Control System?
* **File System**: A storage system that organizes and manages files on a device. Changes need to be managed manually.

* **Version Control System**: Track changes automatically, manage versions and help collaborate with team members easily.

## What is the difference between `git push -u origin main` and `git push origin master`?
* `git push -u origin main`: This will push the local `main` branch to the remote `main` branch and set it as the default upstream branch for future pushes.

* `git push origin master`: The changes are pushed to the `master` branch, without setting it to be the default upstream branch.

## What is the difference between `git remote set-url origin` and `git remote add origin`?
* `git remote set-url origin <url>`: Sets the URL for an existing remote named `origin`.

* `git remote add origin`: Adds a new remote repository with the name `origin`.

## What is the difference between Clone and Fork in GitHub?
* **Clone**: Copies a repository to your local machine to work on it.

* **Fork**: Makes a copy of someone else's repository under your own GitHub account for independent development.

## What are branching Strategies?
Branching strategies are the defined ways that teams use branches in Git during development. Common approaches include:

* **Feature Branching**: One branch per feature.
* **Git Flow**: Structured workflow with branches like `main`, `develop`, and feature branches.
* **Trunk-Based Development**: Work directly on the main branch with ephemeral feature branches.

## What is the difference between fetch and pull?
* **Fetch**: Retrieve changes from a remote repository but does not merge them.
* **Pull**: Combines `fetch` and `merge`, downloading and merging changes into your local branch.

## What are Git Hooks?
Git Hooks are scripts that run automatically at specific events in the Git workflow, such as before a commit or after a push. They can automate tasks like code formatting or running tests.

## What is a Pre-Commit Hook?
A pre-commit hook is a script that runs before a commit is finalized. It's often used to enforce code quality checks, run linters, or validate files.

## What is GitHub Actions?
GitHub Actions is a CI/CD tool built into GitHub. It allows automating workflows that span building, testing, and deployment according to triggers like commits or pull requests.

## GitLab Vs. BitBucket: What Is the Difference?
* **GitLab**: Focuses on DevOps with features like CI/CD pipelines, container registry, and on-premises hosting.
* **BitBucket**: More geared toward teams that use Atlassian products such as Jira, with deep integration and an enterprise focus.