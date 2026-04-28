# First Footprints
**Track:** Bash | **Level:** L0 (scaffolded L1) | **Date Completed:** 2026-04-28 | **Hints Used:** Tier 1 (offered, self-served via `--help`) | **Time Spent:** ~30m

## What This Was
First Bash challenge. Four micro-tasks covering the absolute floor of terminal use: locate yourself in the filesystem (`pwd`), navigate to a target directory (`cd`), list its contents including hidden files (`ls -a`), read a small file end-to-end (`cat`), and read selected portions of a larger file (`head -n`, `tail -n`). Scaffolded with a toolkit list of six commands; figuring out which one applied to which task was the work.

## What I Built
*(to be filled in by Emre)*

## Key Concepts Used
- **Filesystem navigation:** `pwd`, `cd`, working directory vs absolute paths.
- **Listing:** `ls`, hidden files (dotfiles), the `-a` flag.
- **File reading:** `cat` for full content, `head -n N` for first N lines, `tail -n N` for last N lines.
- **Flags vs arguments:** flags (`-a`, `-n 20`) modify *how* a command behaves; arguments (`.`, `CLAUDE.md`) tell it *what/where* to operate on.
- **Self-service documentation:** every Unix binary supports `--help` and most have a `man` page.

## What I Got Wrong First
*(to be filled in by Emre — mandatory)*

Hint: there are at least two specific things to write about here. The `.` vs `-a` confusion on Task 2, and the `-n 5` vs `-n 10` precision miss on Task 4.

## Weak Points Flagged
- **WP001** — Instruction-precision / end-to-end follow-through. Identified right tool but missed parts of the brief twice in one session (Task 2 listing skipped on round 1; Task 4 line count wrong on round 1). Promoted from WA001 (Python diagnostic). Stage 0, retest 2026-05-02.

## Security Implication Noted
Default `ls` hides exactly the files that matter most in security work — `.bash_history`, `.ssh/`, `.aws/credentials`, `.env`, `.git/config`. The difference between `ls` and `ls -la` is the difference between seeing and not seeing credentials on a real engagement.

## What I Would Do Differently
*(to be filled in by Emre)*

## Final Solution
*(to be filled in by Emre — paste your final commands and outputs)*

---
*Part of the OU Cyber Security practical learning portfolio*
