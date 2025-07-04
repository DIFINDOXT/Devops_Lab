# DevOps Git Workflow - Day 01: Git Branching & Workflow Simulation

## ✅ Objective:
Simulate a professional Git branching model with multiple teams working in a shared repository. Practice real-world DevOps branching workflows using:

- `main` (production-ready)
- `feature/` (new functionality)
- `hotfix/` (bug fixes)
- `release/` (preparing for release)

---

## 🧑‍💻 Developers Simulated:
- `feature/user-auth`: Implements basic login functionality
- `hotfix/fix-login-logic`: Fixes a bug in login condition
- `release/v1.0`: Combines all work for final release

---

## 📂 Folder Structure:

Day-01_Branching-Workflows/
├── config/
│ └── app.conf
├── docs/
├── scripts/
│ └── deploy.sh
├── src/
│ └── app.py
├── tests/
└── Readme-Overview.md

---

## 🔁 Git Flow Simulated:

```text
main
├── feature/user-auth        --> new login feature
│   └── (Merged into release)
├── hotfix/fix-login-logic   --> patch fix
│   └── (Merged into release)
└── release/v1.0             --> tested + tagged → merged into main



🏁 Outcomes:
Practiced feature/hotfix/release strategy

Used git checkout -b, git merge, git log --oneline --graph

Tagged version: v1.0.1

