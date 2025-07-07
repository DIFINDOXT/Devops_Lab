# 📘 Day 3 – Advanced Git Operations

## ✅ Section 3.1: Reset vs Revert vs Checkout

### ✔️ What Was Practiced:
- git checkout <commit>
- git revert <commit>
- git reset --soft HEAD~n
- git reset --hard HEAD~n
- git reset HEAD <file>

### 🧠 Real-World Use Cases:
- Checkout: explore old commit safely
- Revert: undo a bad commit on main branch
- Reset (soft): squash multiple commits into one
- Reset (hard): remove sensitive or broken code
- Reset (mixed): unstage specific files

### 📂 Files Modified:
- src/app.py
- config/app.conf
- README-Day3.md

### 📌 Notes:
- Branch used: main
<<<<<<< HEAD
- No pushes made until section completedMore changes to README
=======

## ✅ Section 3.2: Git Stash Workflows

### ✔️ What Was Practiced:
- `git stash push -m "message"` – Save uncommitted work
- `git stash list` – View all stashes
- `git stash show -p stash@{n}` – View stash details
- `git stash pop` – Apply and remove stash
- `git stash apply stash@{n}` – Apply without removing
- `git stash drop`, `git stash clear` – Cleanup

### 🧠 Real-World Use:
- Safely switch tasks without losing WIP
- Juggle multiple pieces of work without polluting history
- Re-apply stashed changes when feature is resumed

### 📂 Files Modified:
- `src/app.py`
- `config/app.conf`

### 📌 Branches:
- `feature/api-integration`
- `hotfix/security-patch` (created and merged to main)
- No pushes made until section completed...More changes to README

=======

## ✅ Section 3.3: Cherry-picking & Interactive Rebase

### ✔️ What Was Practiced:
- `git cherry-pick <commit>` – Apply selected commits across branches
- `git cherry-pick --continue / --abort / --skip` – Resolve cherry-pick conflicts
- `git rebase -i HEAD~n` – Squash, reorder, or drop messy commits

### 🧠 Real-World Use:
- Use cherry-pick to promote only tested/approved commits to `main`
- Use interactive rebase to clean feature branches before PR/merge
- Avoids polluting team history with junk commits like “wip” or “fix typo”

### 📂 Branch:
- `experiment/performance-tests` (source)
- `demo/messy-commits` (cleaned via rebase)

=======
