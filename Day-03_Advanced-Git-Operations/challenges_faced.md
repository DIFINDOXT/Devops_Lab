# ✅ Challenges Faced – Git Day 3: Reset, Revert, Stash, Cherry-pick, Rebase

This log documents the practical Git challenges encountered while working on destructive and history-rewriting operations. Day 3 involved mastering core Git internals such as `reset`, `revert`, `stash`, `cherry-pick`, and `rebase -i`. The problems and solutions listed below capture what typically goes wrong during production Git workflows and how to recover safely.

---

## 1️Revert vs Reset Confusion

* **Issue**: Ran `git reset --soft HEAD~2` expecting it to remove the revert commit made earlier.
* **Reality**: `reset` only undoes commits from current HEAD, and doesn't affect earlier commits like revert unless they're in the last N HEAD commits.
* **Solution**:

  * Used `git log` to confirm position of revert.
  * Learned `reset` is useful for local rewrites, while `revert` creates new commits and maintains history.

---

## 2️Hard Reset Side Effects

* **Issue**: `git reset --hard HEAD~1` accidentally removed a revert commit and brought back the buggy line in `app.py`.
* **Risk**: Could have lost changes if not backed up.
* **Solution**:

  * Created a backup branch before hard reset (`git branch backup-before-reset`).
  * Used `git reflog` to understand movement of HEAD.

---

## 3️Git Stash Management

* **Issue**: Uncertainty around how stashing preserves multiple change sets.
* **Challenge**: Forgetting to check stash contents before popping caused context loss.
* **Solution**:

  * Used `git stash push -m "message"` for named stashes.
  * Inspected stashes with `git stash show -p stash@{n}`.
  * Practiced `stash apply`, `pop`, `drop`, and `clear` commands.

---

## 4️Cherry-pick Conflict with Deleted File

* **Issue**: While cherry-picking a performance test commit, Git threw an error:

  > `tests/test_performance.py deleted in HEAD and modified in cherry-pick`.
* **Cause**: The file didn’t exist on `main` but existed in source branch.
* **Solution**:

  * Used `git add` to stage the recovered file.
  * Completed the cherry-pick using `git cherry-pick --continue`.
  * Learned when to `--abort` and `--skip` safely.

---

## 5️Interactive Rebase Blocked by Unstaged Changes

* **Issue**: Tried running `git rebase -i HEAD~3` but got blocked due to changes in `README-Day3.md`.
* **Solution**:

  * Either committed the file as WIP before rebasing, or stashed it.
  * Used `git stash push -m "Temp stash before rebase"` to isolate changes.

---

## 6️Nano Rebase Message Confusion

* **Issue**: Git opened nano after squash step during rebase, asking for combined commit message.
* **Confusion**: User was unsure if this was an error.
* **Solution**:

  * Understood nano is used for finalizing the squashed commit message.
  * Used `Ctrl+O`, `Enter`, and `Ctrl+X` to save and exit.

---

## 7️Committed to Wrong Branch (`demo/messy-commits`)

* **Issue**: Made a commit (README for Day 2) on the wrong branch.
* **Goal**: Wanted the commit on `main`.
* **Solution**:

  * Used `git cherry-pick <commit-hash>` from `main` to recover.
  * Resolved conflict in `README-Day3.md` using manual merge.

---


> 💡 **Takeaway**: Day 3 simulated real-world destructive Git operations and taught how to use `reset`, `stash`, `rebase`, and `cherry-pick` with caution. It emphasized safety tools like `reflog`, naming stashes, and tagging checkpoints for rollback. This level of workflow is what recruiters and engineers expect in team collaboration and CI/CD pipelines.
