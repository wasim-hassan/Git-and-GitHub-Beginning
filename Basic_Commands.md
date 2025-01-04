## Basic Git Commands
* Configures the username for all Git repos on your computer. Use your name or handle.
```bash
git config --global user.name "your - username"
```

* Configures the email for commits globally. It identifies who made the changes.
```bash
git config --global user.email "your email"
```

* Start a new Git repository in your project directory. This creates a .git folder to track changes.
```bash
git init
```

* Displays the status of your repository. You can see staged, unstaged, and untracked files.
```bash
git status
```

* Stages a specific file for the next commit.
```bash
git add <filename>
```

* Stages all changes in the current directory (tracked and untracked files).
```bash
git add .
```
* Commits the staged changes with a message describing the changes.
```bash
git commit -m "Your message"
```

* Removes a file from the staging area but leaves it in the working directory.
```bash
git rm --cached <filename>
```

* Restores changes to a file, reversing changes.
```bash
git restore <filename>
```

## Pushing to GitHub
* It sets a remote repository URL as "origin".
```bash
git remote add origin <your-GitHub-url>
```

* Lists the URLs of the remote repositories linked to your local repository.
```bash
git remote -v
```

* Add your repository's remote url. Here push/pull codes in here
```bash
git remote add origin https://github.com/your-github-username/your-github-repository-name.git
```

* Re-names current branch into main (used often with repository for new names at creation.)
```bash
git branch -M main
```

* Replace an access token authentication into remote update url in push secure process for GitHub.
```bash
git remote set-url origin https://Your-Access-Token-Key@github.com/your-github-username/your-github-repository-name.git

```

* Pushes your local main branch to the main branch on the remote repository and sets it as the default upstream branch.
```bash
git push -u origin main
```

## Cloning a Repository
* Downloads a repository and its history from the given URL.
```bash
git clone <the-url>
```

## Pulling Changes
* Fetches and merges changes from the remote main branch to your local branch.
```bash
git pull origin main
```

## Branching
* Lists all local branches in your repository.
```bash
git branch
```

* Makes a new branch with the name provided.
```bash
git branch <branch-name>
```

* Switches to the given branch. (Instead of git checkout to switch branches.)
```bash
git switch <branch-name>
```

* Create and switch to a new branch if it doesn't exist, or just switch to it if it does.
```bash
git checkout -B <branch-name>
```

## Viewing Logs
* Shows the commit history with author, date, and message.
```bash
git log
```

* Shows a simplified, one-line-per-commit log.
```bash
git log --oneline
```

## Fetching and Pulling
* Downloads updates from the remote repository without merging them into your local branch.
```bash
git fetch
```

* Combines `git fetch` and `git merge` to download and merge changes from the remote branch.
```bash
git pull
```

## Rebasing
* Fetches and merges changes from the remote main branch.
```bash
git pull origin main
```

* Fetches changes and applies them on top of your local commits, rewriting commit history.
```bash
git pull origin main --rebase
```