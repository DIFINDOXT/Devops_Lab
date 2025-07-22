# 🧪 DevopsLab Git Mastery – Hands-on Git Simulation Project

Welcome to the **DevopsLab** repository – a structured, multi-day hands-on simulation for mastering Git like a real DevOps engineer. This repo demonstrates core Git concepts across 5 progressive days of learning with actual project files, real branching logic, GitHub workflows, recovery commands, and team collaboration scenarios.

---

## 📁 Repository Structure

DevopsLab/
│
├── Day-01_Branching-Workflows/
│ ├── Readme-Overview.md # Daily intro + branching flow
│ ├── challenges_faced.md # Issues faced and solved
│ ├── src/, config/, scripts/, tests/
│
├── Day-02_Merge-Conflicts/
│ ├── README.md
│ ├── challenges_faced.md
│ └── config/
│
├── Day-03_Advanced-Git-Operations/
│ ├── README-Day3.md
│ ├── challenges_faced.md
│ ├── src/, config/, docs/, scripts/, tests/
│
├── Day-04_Remote-Collaboration/
│ ├── Readme.md
│ ├── challenges_faced.md
│ ├── contributor-clone/ # Simulated contributor clone
│ ├── devops-project-remote/ # Actual bare Git remote repo
│ ├── devops-project-sim/ # Simulated local repo for remote testing
│ ├── final-code/, final-config/, final-docs/
│
├── Day-05_Git-Hooks-History-Management/
│ ├── README.md
│ ├── challenges_faced.md
│ ├── hooks/ # Custom pre-commit, post-commit
│ ├── src/, config/
│
├── logs/
│ └── commit.log # Auto-generated via Git hook
│
└── Readme-Overview.md


---

## 🎯 Project Goals

- ✅ Simulate Git workflows used by DevOps engineers & teams
- ✅ Practice `branch`, `merge`, `rebase`, `reset`, `stash`, `cherry-pick`
- ✅ Resolve real merge conflicts across feature/hotfix branches
- ✅ Simulate GitHub-like remote collaboration (Day 4)
- ✅ Explore Git hooks (`pre-commit`, `post-commit`) and log automation
- ✅ Recover lost commits, deleted branches using `reflog`
- ✅ Maintain professional, interview-ready structure and documentation

---

## 🗓️ Day-wise Git Mastery Topics

| Day | Theme                                  | Key Concepts Covered |
|-----|----------------------------------------|----------------------|
| 1   | Branching & Workflows                  | `main`, `feature/`, `hotfix/`, `release/` |
| 2   | Merge Conflicts & Resolution           | 3-way merges, PR simulations |
| 3   | Advanced Git Operations                | `reset`, `stash`, `cherry-pick`, `rebase -i` |
| 4   | Remote Collaboration & GitHub Flow     | bare repo, clone, push/pull, conflict handling |
| 5   | Git Hooks & History Management         | `pre-commit`, `post-commit`, `reflog`, interactive rebase |

---

## 📌 How to Use This Repo

1. Clone the repo:
   ```bash
   git clone git@github.com:<your-username>/DevopsLab.git
   ```

2. Go into any Day-XX_* folder to explore that simulation:
   ```
   cd Day-03_Advanced-Git-Operations/
   ```

   **Read:**

- README.md → instructions for the day
- challenges_faced.md → issues + solutions (good for interviews)
- Run Git commands and scripts to simulate the actions.

---

## 🤝 Ideal For

- DevOps engineers learning real-world Git flows
- Anyone preparing for interviews or Git certifications
- Self-learners looking to simulate team collaboration locally
- Contributors wanting a clean, extensible Git project template

---

## ⭐ Star & Fork
If you find this project helpful:

- 🌟 Star the repo
- 🍴 Fork and try the simulations on your own
- 🧠 Learn by breaking, fixing, and documenting

**Maintained by Shubhadeep Bhowmik**
GitHub: github.com/shubhadeepxt
