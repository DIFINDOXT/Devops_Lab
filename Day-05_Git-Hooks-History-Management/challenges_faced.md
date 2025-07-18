# ✅ Challenges Faced – Git Day 5: Git Hooks, History Management & Interview Scenarios

This log documents the technical and workflow challenges encountered while implementing Git hooks (`pre-commit`, `post-commit`), cleaning history via interactive rebase, recovering lost commits/branches, and preparing for Git interview scenarios.

---

## 1 Git Hook Activation Issues

- **Issue**: Created hook scripts in the `hooks/` folder under `Day-05_Git-Hooks-History-Management`, but Git didn’t run them.
- **Cause**: Git only runs hooks placed inside `.git/hooks/` and named exactly as expected (`pre-commit`, `post-commit`, etc.).
- **Solution**:
  - Copied custom scripts from `hooks/` to `.git/hooks/` using:
    ```bash
    cp hooks/pre-commit ../.git/hooks/pre-commit
    ```
  - Made sure the files had execute permissions:
    ```bash
    chmod +x .git/hooks/pre-commit
    ```

---

## 2 Python Not Found in Pre-Commit Hook

- **Issue**: Pre-commit hook failed with:
  `python: command not found`
- **Cause**: WSL defaults to Python 3 as `python3`, but the script called `python`.
- **Solution**:
  - Updated `pre-commit` script to use `python3 -m py_compile` instead.
  - Re-copied the updated file to `.git/hooks/`.

---

## 3 Pre-Commit Hook Aborted Commits Due to TODO Comments

- **Issue**: Hook detected `TODO` in staged files and aborted the commit.
- **Impact**: Couldn’t proceed without either resolving or overriding the TODO.
- **Solution**:
  - Prompted user interaction added via:
    ```bash
    read -p "Continue anyway? (y/n): " -n 1 -r
    ```
  - Used `y` to force the commit if necessary during development.

---

## 4 Post-Commit Hook Triggered Unexpectedly During Rebases

- **Issue**: Post-commit hook triggered on squash/rebase commits, cluttering `logs/commit.log`.
- **Learned**:
  - Git runs post-commit on every created commit, including automated ones during rebase.
  - Can optionally check for interactive session or rebase state to avoid noisy logs.

---

## 5️ Interactive Rebase Blocked by Unstaged Changes

- **Issue**: Running `git rebase -i HEAD~4` threw:
  `error: cannot rebase: You have unstaged changes`
- **Cause**: Post-commit hook was logging commit output into `logs/commit.log`, which remained modified after each commit.
- **Solution**:
  - Staged the log file before rebase:
    ```bash
    git add logs/
    git commit -m "chore: update commit logs"
    ```

---

## 6 Git History Messiness Before Tagging

- **Issue**: Multiple similar commit messages (`Part1`, `Part2`, `Part3`) made the history look noisy before tagging.
- **Solution**:
  - Squashed commits using:
    ```bash
    git rebase -i HEAD~3
    ```
  - Combined into a single clean commit before tagging:
    ```bash
    git tag -a v5.2-post-commit -m "Post-commit hook with local logging"
    git push origin v5.2-post-commit
    ```

---

## 7️ Git Reflog Recovery Simulation

- **Issue**: Simulated a `git reset --hard` accidentally deleted a commit.
- **Solution**:
  - Used `git reflog` to identify the lost commit hash.
  - Recovered using:
    ```bash
    git cherry-pick <commit_hash>
    ```

---

## 8️ Branch Deletion Recovery

- **Issue**: Simulated branch deletion (`git branch -D temp-branch`) and needed to recover.
- **Solution**:
  - Used `git reflog` to find the last commit on the deleted branch.
  - Restored branch with:
    ```bash
    git checkout -b temp-branch <commit_hash>
    ```

---

## 9️ Git Blame Failed to Parse Function

- **Issue**: Tried running:
    git log -L :check_todos:pre-commit
  but got error: `no match`
- **Cause**: The logic wasn’t written as a named function.
- **Solution**:
  - Switched to using line range syntax:
    ```bash
    git log -L 10,20:hooks/pre-commit
    ```
  - Learned that `-L :funcname:file` only works on real named functions.

---

> 💡 **Takeaway**: Day 5 simulated real-world Git automation, recovery, cleanup, and interview query workflows — making this a complete GitOps-ready exercise. It’s now production-grade, push-ready, and understandable by peers, mentors, and recruiters.
