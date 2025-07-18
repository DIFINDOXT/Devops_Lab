# ⚔️ Day 02: Git Merge Conflict — Challenges Faced & Solutions

This file documents the challenges encountered during Day 2 of the Git Mastery Practice series. The goal was to simulate a real merge conflict between developers and resolve it using both GitHub UI and CLI. The journey included multiple learning curves, edge cases, and valuable takeaways.

---

## 🧭 Goal of Day 2

- Simulate two developers working on the same file (`config/app.conf`)
- Trigger a **real** Git merge conflict
- Resolve the conflict **manually via CLI**
- Document and screenshot everything for DevOps portfolio

---

## 🚧 Challenges Faced

### 1. 🔄 Git Fast-Forward Merge Prevented Conflict

**Problem:**
We expected a merge conflict between `dev1` and `dev2` branches, but Git merged cleanly without any conflict.

**Cause:**
`dev1` was merged into `dev2` *before* `dev2`'s changes were committed. Git saw both sets of changes in one linear history and performed a **fast-forward merge**.

**Impact:**
No conflict occurred — defeating the purpose of Day 2 simulation.

**Solution:**
Avoid merging `dev1` into `dev2`. Instead, both branches should branch directly from `main`, modify the **same lines**, and push independently.

---

### 2. 🔍 GitHub UI Still Showed “No Conflicts”

**Problem:**
Even after rewriting `app.conf` in `dev3`, GitHub still allowed an automatic merge.

**Cause:**
Git was smart enough to see that line changes were not overlapping (e.g., modifying different sections or replacing full blocks).

**Solution:**
Force a real conflict by:
- Creating `dev3` from `main`
- Modifying **the exact same lines** as `main`
- Pushing `dev3` independently
- Then merging `main` → `dev3`

✅ This triggered the true conflict

---

### 3. 🧹 Local Branch Didn’t Show GitHub Folder

**Problem:**
`Day-02_Merge-Conflicts/` folder was not visible in some branches or in the GitHub UI.

**Cause:**
The folder was only committed inside `dev1/database-config`. It wasn’t present in `main` or other branches.

**Solution:**
Merge `dev1` into `main` first or re-create the folder in other branches.  
✅ Merged `dev1` with `--no-commit` to bring the folder in safely.

---

### 4. ❓Unexpected Untracked File: main
**Problem:**
git status showed Untracked file: main causing confusion.

**Cause:**
Accidentally created a file named main using > main or bad redirect.

**Solution:**
Removed with:
`rm main`



### 5. 🧶 Merge Conflict Resolution (Final Step)
**Problem:**
Manual conflict resolution required editing <<<<<<<, =======, and >>>>>>> lines carefully.

**Solution:**
Used vim to:

Review both versions

Combine or choose appropriate lines

Save file and mark as resolved


## 🧠 Lessons Learned
- Not all merges cause conflicts — Git is smarter than expected.
- Avoid merging branches into each other before conflict simulation.
- Editing different blocks won't always cause conflict — focus on the same lines.
- GitHub UI and CLI both behave differently in merge flows.
- Real DevOps engineers resolve conflicts locally — not via GUI alone.

## 🏁 Outcome
A true conflict was simulated and resolved manually
All changes merged to main safely
Repo cleaned: old branches deleted, main protected
Screenshots taken for GitHub, Twitter, and README documentation

📌 Keywords
merge conflict, resolve conflict, devops, git branching, manual resolution, fast-forward, ssh-add, untracked file, vim merge
