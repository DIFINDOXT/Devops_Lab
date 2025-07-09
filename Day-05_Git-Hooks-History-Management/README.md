# DevOps Git Mastery - Final Day

## Git Hooks Implemented

### 🔹 Pre-commit Hook
- Validates Python syntax using `python3 -m py_compile`
- Blocks commits if `TODO`, `FIXME`, or `HACK` comments are found
- Skips `.pyc` and large files for efficiency

### 🔹 Post-commit Hook
- Logs each successful commit into `logs/commit.log`
- Shows commit hash, message, and files changed
- Simulates team notification (email placeholder)

### 🔹 Rebase Strategy
- Used `git rebase -i HEAD~4` to squash multiple minor commits
- Final tag: `v5.2-post-commit`

