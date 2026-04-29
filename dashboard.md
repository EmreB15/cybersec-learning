# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-04-28 — after Session 3 (Bash L0 challenge 2)*

---

## 🎯 Pickup Here

**Next session: Bash L0 challenge 3 of 3.**

> 🔧 **Open question to resolve at session start:** Keep at L0 scaffolding, or fold challenge 3 into a normal-difficulty L1 challenge?
> Strong indicators for promotion: zero hints on Tasks 1–3 of challenge 2; Tier 1 reframe + self-correction on Task 4; unprompted "is this hard-coded?" elegance reflection; NDG Linux Unhatched course covering permissions and file reading externally.
> Decide before the challenge is designed.

> ⚠️ **WP001 + WP002 retests both fire 2026-05-02.** If next session is on or after Saturday, both retests run before any new content.

**Side task (optional, portfolio polish):**
- Archive `bash-L0-first-footprints` — substitute the real path for the `<target>` placeholder in Final Solution. *(`bash-L0-trail-in-the-logs` archived 2026-04-28 ✓)*

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | L1 | ░░░░ 0/4 | 0 | 🟢 Ready to start |
| 🖥️ Bash | L0 (scaffolded L1) | ██░ 2/3 | 2 | 🟢 In progress, promotion under review |
| 🔐 Concepts | L1 | ░░░ 0/3 | 0 | 🟢 Ready to start |
| 🎭 Scenarios | — | Locked | 0 | 🔒 |

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Retest Due |
|----|-------|-------|-------|------------|
| WP001 | cross-track | Instruction-precision / end-to-end follow-through — identifies right tool but misses sub-tasks or uses wrong parameter values | 0 | **2026-05-02** |
| WP002 | bash | Frequency-count pipelines: missing count-column sort or using lexicographic instead of numeric (`sort -r` vs `sort -nr`); trusts pipeline output without inspecting intermediate stages | 0 | **2026-05-02** |

**WP001 evidence:**
- Diagnostic task 3 (Python string split) — partial assembly
- Bash L0 First Footprints Task 2 round 1 — skipped listing entirely
- Bash L0 First Footprints Task 4 round 1 — used `-n 5` instead of `-n 10`

**WP002 evidence:**
- Trail in the Logs Task 4 round 1 — `sort | uniq -c | head -n 1` returned alphabetical-first IP, not most-frequent IP
- Trail in the Logs Task 4 round 2 — `sort -r` used; works on single-digit counts only, would silently misrank ≥10 due to lexicographic comparison
- *Self-correction observed mid-task:* user flagged elegance concern unprompted ("hard coded in a sense"). Track whether retest confirms it stays self-corrected.

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
| 2026-05-02 | WP002 (frequency-count pipelines) | bash | 0 → 1 if pass |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [ ] All tracks reach Level 1 complete
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups

---

## 🗺️ Up Next

**Bash:** Challenge 3 (level TBD pending calibration). Likely topics: scripted/looped log analysis, redirection, exit codes — bridging from one-liners to small reusable scripts.
**Concepts (L1):** First challenge is a full phishing analysis with a systematic indicator framework — direct response to WA002.
**Python (L1):** First challenge will be a log file reader or password strength evaluator — pick when you have a longer block. Cross-track note: Python's `collections.Counter.most_common(N)` does what `sort | uniq -c | sort -nr | head -n N` does in one line.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**3 logged.**

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]` or `[-N:]`. Bash version is a pipe-ready one-shot; Python version composes inside larger scripts.
- *2026-04-28* — **Bash ↔ Python**: frequency analysis. Bash: `... | sort | uniq -c | sort -nr | head -n N`. Python: `collections.Counter(iterable).most_common(N)`. **Same gotcha in both**: default sort/min/max on numeric strings is lexicographic — `sorted(['10','9'])` returns `['10','9']` in Python too. Convert to int first.
- *2026-04-28* — **Bash ↔ Python**: positional field extraction is fragile. `awk '{print $11}'` and `line.split()[10]` both break the moment log format shifts a column. Real-world fix in either language is regex extraction (`grep -oE` / `re.search`) targeting the value's *shape*, not its *position*.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box)
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — not yet installed. **Required before any scanning / network challenge.**

---

## 📁 Portfolio Stats

- Write-ups generated: 2
- Write-ups archived (with reflections filled): 1
- Total challenges completed: 2
- Total sessions: 3
- Total hours: ~2.0
