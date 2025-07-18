# ✅ Challenges Faced – Git Day 4: Remote Collaboration & Remote Strategies

This log captures the real-world challenges encountered during the simulation of Git-based remote collaboration using bare repositories, multiple remotes, and merge workflows. This setup mimics a production-like DevOps scenario.

---

## 1️Nested Git Repositories Created Accidentally

- **Issue**: Git was initialized inside subfolders (`devops-project-sim`, `devops-project-remote`, `contributor-clone`) which were inside the main Git repo (`DevopsLab`).
- **Impact**: Led to nested `.git` folders that made it impossible to push `DevopsLab` as a single clean repo. GitHub showed errors and failed pushes.
- **Solution**:
  - Removed `.git` folders from sub-projects manually using:
    rm -rf devops-project-sim/.git
    rm -rf devops-project-remote/.git
    rm -rf contributor-clone/.git
  - Preserved only final source code from each simulation using:
    cp -r devops-project-sim/src final-code/
    cp -r devops-project-sim/config final-config/
    cp -r devops-project-sim/docs final-docs/

---

## 2 Git fetch vs pull vs merge – Visibility Confusion

- **Issue**: Misunderstanding on what gets updated where when using:
    git fetch
    git pull
    git merge
- **Clarified**:
  - git fetch: Gets remote changes into tracking branch only (doesn’t affect local working branch).
  - git merge upstream/main: Applies fetched commits to your local branch.
  - git pull: Combines fetch + merge.
- **Commands Practiced**:
    git fetch origin
    git log origin/branch-name --oneline --graph
    git diff HEAD..origin/branch

---

## 3 Git Credential Errors During Fetch

- **Issue**: Running `git fetch` from the CLI suddenly prompted for credentials again:
    git: 'credential-manager-core' is not a git command.
- **Impact**: Fetch failed; halted flow mid-way.
- **Solution**:
  - Re-entered GitHub credentials using PAT.
  - Cached credentials using:
    git config --global credential.helper store

---

## 4 Final Cleanup Strategy Was Unclear

- **Issue**: Needed a clean way to preserve all Day 4 work without pushing `.git` folders.
- **Solution**:
  - Created folders: final-code/, final-config/, final-docs/
  - Wrote a README.md summarizing Day 4 logic
  - Pushed only from main DevopsLab repo to avoid nested Git issues
  - Ensured `.git` folders were removed using:
    find . -name ".git" -type d

---

## 5 Visual Evidence Not on GitHub

- **Issue**: Recruiters wouldn’t see Day 4 commits since work was done in subfolders.
- **Solution**:
  - Took terminal screenshots
  - Preserved commit history via git log --oneline --graph
  - Uploaded screenshots to Day-04_Remote-Collaboration/screenshots/ (optional)
  - Added proper Day 4 summary in README.md so GitHub still reflects effort

---

💡 Takeaway: Day 4 exposed real-world problems like nested Git issues, remote auth failures, and fetch-merge misunderstandings. Solving them added strong DevOps confidence for remote workflows and Git collaboration.
