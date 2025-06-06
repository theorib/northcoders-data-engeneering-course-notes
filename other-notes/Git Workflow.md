# Git Workflow Guidelines

## Before creating a pull request from a feature branch

1. Switch into the branch we want to create the pull request
    ```bash
    git switch feature-branch-name
    ```

2. Get latest changes from origin if the branch is online and you are collaborating with someone else
    ```bash
    git fetch origin
    ```

3. Rebase the feature branch onto the latest version of the main branch
    ```bash
    git rebase origin/main
    ```

4. If there are conflicts, resolve them and then
    ```bash
    git add files_that_you_resolved_conflics
    ```

5. Continue the rebase
    ```bash
    git rebase --continue
    ```

6. Repeat step 4 until all conflics are resolved and rebase is finished

- Don't use git pull origin main while on a feature branch - this creates merge commits
- Use git rebase origin/main instead to keep a clean linear history
- Only pull once after fetching - don't keep pulling to "make sure you're up to date"

## if you have too many conflics and are stuck in a rebase loop:
Find the commits you want to integrate into main and copy their commit hashes. You can achieve this with git
1. Create a brand new branch to help out
    ```bash
    git switch main
    git pull origin main
    git checkout -b feature-branch-name-clean
    ```
2. Cherry pick only the commits you want:
    ```bash
    git cherry-pick commit-hash-1 commit-hash-2
    ```

### If you want to edit those commits instead of just accepting them, you can edit them one by one with:
```bash
git cherry-pick --no-commit commit-hash
```

## Other useful workflows
### If you deleted a remote branch and want to reset the links of your local branch so it's not connected with any ghost remote branches there are a few options:

1. Remove the remote reference
    ```bash
    git switch branch-to-fix
    git branch --unset-upstream
    ```
2. Clean up all stale remote references
    ```bash
    git remote prune origin
    ```

- To check if a remote branch exists:
```bash
git branch -r
```

git reset --hard <commit-hash>