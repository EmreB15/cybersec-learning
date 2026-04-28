# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-04-28 — after Session 2 (Bash L0 challenge 1)*

---

## 🎯 Pickup Here

**Next session — choose a track:**
1. **Bash L0 challenge 2 of 3** (pipes + grep on a small log file). Continues the in-progress track.
2. **Concepts L1 phishing analysis** — quick warm-up, lowest friction.
3. **Python L1 challenge 1** — strongest existing skill, save for a longer block.

**Side task:** archive the `bash-L0-first-footprints` write-up by filling in the four user-fillable sections.

> ⚠️ **WP001 retest fires 2026-05-02.** That runs first whatever track you pick that day.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | L1 | ░░░░ 0/4 | 0 | 🟢 Ready to start |
| 🖥️ Bash | L0 (scaffolded L1) | █░░ 1/3 | 1 | 🟢 In progress |
| 🔐 Concepts | L1 | ░░░ 0/3 | 0 | 🟢 Ready to start |
| 🎭 Scenarios | — | Locked | 0 | 🔒 |

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Retest Due |
|----|-------|-------|-------|------------|
| WP001 | cross-track | Instruction-precision / end-to-end follow-through — identifies right tool but misses sub-tasks or uses wrong parameter values | 0 | **2026-05-02** |

**WP001 evidence so far:**
- Diagnostic task 3 (Python string split) — partial assembly
- Bash L0 Task 2 round 1 — skipped listing entirely
- Bash L0 Task 4 round 1 — used `-n 5` instead of `-n 10`

---

## 👀 Watch-Areas (pre-weak-point)

| ID | Track | Observation | Source |
|----|-------|-------------|--------|
| WA002 | Concepts | Phishing indicator list is partial (misses link inspection, missing specifics, vague sign-off) | Diagnostic task 5 |

*WA001 promoted to WP001 on 2026-04-28.*

---

## 📅 Retests Scheduled

| Date | Weak Point | Track | Stage |
|------|-----------|-------|-------|
| 2026-05-02 | WP001 (instruction-precision) | cross-track | 0 → 1 if pass |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [ ] All tracks reach Level 1 complete
- [ ] Lab environment set up (VirtualBox + Metasploitable2)
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups

---

## 🗺️ Up Next

**Bash (L0):** Challenge 2 will introduce pipes (`|`) and `grep` — taking the navigation/reading skills you have and chaining them to extract specific patterns from files. This is where Bash starts feeling powerful.
**Concepts (L1):** First challenge is a full phishing analysis with a systematic indicator framework — direct response to WA002.
**Python (L1):** First challenge will be a log file reader or password strength evaluator — pick when you have a longer block.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**1 logged.**

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]` or `[-N:]`. Bash version is a pipe-ready one-shot; Python version composes inside larger scripts.

---

## 📁 Portfolio Stats

- Write-ups generated: 1
- Write-ups archived (with reflections filled): 0
- Total challenges completed: 1
- Total sessions: 2
- Total hours: ~1.3
