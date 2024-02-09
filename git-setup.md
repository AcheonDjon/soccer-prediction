# Git Setup and Basic Usage Instructions

## Prerequisites

1. Install [Git](https://git-scm.com/downloads) on your machine.

## Steps to Setup Git

1. Open a terminal.

2. Configure your Git username using the following command. Replace `your_username` with your actual username:

    ```bash
    git config --global user.name "your_username"
    ```

3. Configure your Git email using the following command. Replace `your_email@example.com` with your actual email:

    ```bash
    git config --global user.email "your_email@example.com"
    ```
## Steps to Clone a Repository, Commit Changes, and Push

1. Navigate to the directory where you want to clone the repository.

2. Clone the repository using the following command. Replace `https://github.com/username/repository.git` with your repository's URL:

    ```bash
    git clone https://github.com/BigCobra/soccer-prediction.git
    ```

3. Navigate into the cloned repository:

    ```bash
    cd repository
    ```

4. Create a new file or modify an existing one.

5. Stage the changes for commit:

    ```bash
    git add .
    ```

6. Commit the changes:

    ```bash
    git commit -m "Your descriptive commit message"
    ```

7. Push the changes to the repository:

    ```bash
    git push
    ```

Remember to replace `Your descriptive commit message` with a message describing what changes you made.

For more detailed instructions, refer to the [Git documentation](https://git-scm.com/doc).


You can check the status of your Git repository by using the git status command in your terminal. Here's how:

Open a terminal.
Navigate to your Git repository directory using the cd command. For example, if your repository is in a directory named my-repo, you would use cd my-repo.

Once you're in your repository's directory, run the git status command.

git status 

This command will show you the current state of your repository, including which files have changes that are staged for the next commit, which files have changes that are not yet staged, and which files are not being tracked by Git.