# Git & GitHub Basics

## Contains
1. Git & GitHub Concepts
2. Basic Commands of Git
3. Pull Request & Merging, Branching Strategies
4. Hooks (Pre-commit Hooks)
5. GitLab vs BitBucket. What's the difference?
6. [PROJECT](https://github.com/wasim-hassan/Appetizzer-Website) Deploying a website using GitHub Action and AWS S3 Bucket


## Git & GitHub setup
1. Download Git from the [office site](https://git-scm.com/downloads)
2. Verify Git is installed properly in your system by checking the version:

```bash
git --version
```
Output:
![alt text](<Images/Screenshot-1.png>)

3. Sign up or login to your [GitHub](https://github.com/) account

### Creating File & Folder Using

![alt text](Images/image-1.png)

> 💡 **Note:** VS Code Editor must be installed in the system

1. Create a folder named `github-for-practice` and open the folder with VS Code Editor
2. Create a python file in that folder e.g., `testing.py`

![alt text](Images/Screenshot-7.png)

3. Make the Folder Version Control System:

```bash
git init
```
Output:
![alt text](<Images/Screenshot-2.png>)

4. Verify the Git VSC directory is properly created:

```bash
ls -a
```
Output:
![alt text](Images/Screenshot-3.png)

5. View the untracked files, which my show in red highlight:

```bash
git status
```
Output:
![alt text](Images/Screenshot-4.png)

> 💡 **Note:** The target is to move the `testing.py` from untracked to tracked status

6. Add the python file to **staging** and make it trackable:

```bash
git add testing.py
```
Output:
![alt text](Images/Screenshot-5.png)

7. If you want to revers the changes and make it **unstaged** the:

```bash
git rm --cached testing.py
```

8. Add the python file to **Git VCS**

```bash
git commit -m "added test file"
```

Output:
![alt text](Images/Screenshot-8.png)

9. Adding another .txt file with git commands:
![alt text](Images/Screenshot-9.png)

10. Committing the .txt file:
![alt text](Images/Screenshot-10.png)


### Pushing the files and changes to GitHub
![alt text](Images/Screenshot-11.png)

1. Create a repository in the GitHub
![alt text](Images/Screenshot-12.png) 

![alt text](Images/Screenshot-13.png) 

![alt text](Images/Screenshot-14.png)
![alt text](Images/Screenshot-15.png)

After creating the repository you may find a screen like this one:
![alt text](Images/Screenshot-16.png)


2. Create a token access key:

* Click on th profile icon.
![alt text](Images/Screenshot-17.png)

* Click on Settings
![alt text](Images/Screenshot-18.png)

* Scroll Down and Select Developer settings
![alt text](Images/Screenshot-19.png)

* Create a Personal Access Token
![alt text](Images/Screenshot-20.png)

* Give a name, expiry date and scope of the Personal Access Token
![alt text](Images/Screenshot-21.png)

* Generate the token key
![alt text](Images/Screenshot-22.png)

* Copy the key and secure it with a notepad
![alt text](Images/Screenshot-23.png) 


3. Pushing the code the GitHub repository

```bash
git remote set-url origin https://github.com/your-github-username/your-github-repository-name.git

git branch -M main

git remote set-url origin https://Your-Access-Token-Key@github.com/your-github-username/your-github-repository-name.git

git push -u origin main
```
Output:
![alt text](Images/Screenshot-24.png)

Refresh the GitHub repository and it may look like this one:
![alt text](Images/Screenshot-25.png)

### Pulling Changes from GitHub to local
If you you made a changes using the GitHub GUI, as shown in the image.


* You can pull the changes to your local machine in the following way
![text](Images/Screenshot-26.png) ![text](Images/Screenshot-27.png)

* Enter the pull command in the terminal, and it will pull the changes to the local machine:

```bash
git pull origin main
```
Output:
![alt text](Images/Screenshot-28.png)






