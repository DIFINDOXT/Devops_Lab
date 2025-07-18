# ✅ Challenges Faced – Git Day 1: Branching Strategies & Workflows

This log captures the real-world problems encountered during the setup and simulation of Git branching strategies using `main`, `feature`, `release`, and `hotfix` branches. Each challenge helped reinforce deeper Git knowledge.

---

## 1️1Git Repo Initialization Mistake

- **Issue**: Git was initialized inside `Day-01_Branching-Workflows`, instead of the root `DevopsLab` folder.
- **Impact**: Caused nested Git repositories (`.git` inside `.git`) and made the folder invisible to GitHub when pushing.
- **Solution**:
  - Deleted the repo.
  - Re-initialized Git properly inside `/DevopsLab` (top-level).
  - Confirmed `.git` only exists at the root using `git rev-parse --show-toplevel`.

---

## 2 Authentication Errors While Pushing

- **Issue**: Git asked for GitHub password (which is deprecated), and then denied SSH access.
- **Impact**: Couldn’t push to the GitHub repo using HTTPS or SSH.
- **Solution**:
  - Removed origin and re-added using SSH.
  - Generated new SSH key, added it to GitHub under `Settings → SSH & GPG keys`.
  - Used:
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

---

## 3 Missing Files in GitHub Repo

- **Issue**: Files were not visible on GitHub even after push.
- **Cause**: Either files were added inside a nested repo or not properly committed.
- **Solution**:
  - Verified structure with `tree`.
  - Ensured everything is under the root Git repo (`DevopsLab`) before adding and committing.
  - Reorganized folders and re-added using `git add .` and `git commit -m`.

---

## 4 Merge and Feature Flow Confusion

- **Issue**: Confusion over who should push which branch and where to merge.
- **Clarification**:
  - Developer works on `feature/branch`, then raises PR → `main`.
  - DevOps merges it to `main` and creates `release/v1.0` from there.
  - Any bug in production is handled via `hotfix`, which is merged into both `release` and `main`.

---

## 5 Utracked Nested Folders

- **Issue**: Warning about adding an embedded Git repo:
  > "You’ve added another Git repository inside your current repository."
- **Solution**:
  - Verified using `ls -a` and `tree`.
  - Removed it from the index with:
    ```bash
    git rm --cached <nested-folder-path>
    ```

---

##  Version Tagging Logic

- **Issue**: Confusion between branch pushes and tag pushes.
- **Clarified**:
  - `git push origin release/v1.0` — pushes branch.
  - `git tag -a v1.0.0 -m "Production release"`
  - `git push origin v1.0.0` — pushes annotated tag.
- **Learned**: Tags simulate production release snapshots.

---

## 7 Final Cleanup & Validation

- **Issue**: Wanted to verify if everything is correct and nothing pending.
- **Solution**:
  - Checked each branch with:
    ```bash
    git checkout <branch>
    git fetch --all
    git status
    ```
  - Used `git branch --merged` to see merge state.
  - Final structure confirmed with `tree`.

---

> 💡 **Takeaway**: Day 1 gave a strong foundation in branching flows, GitHub collaboration, UI/CLI integrations, and recovering from real-world Git mistakes.
