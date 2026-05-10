# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-05-10 — after Session 7 (Evidence Trail closes Bash L1; Brute Force Source = Python L1 #2; two write-ups archived; 5h target hit on weekly summary)*

---

## 🎯 Pickup Here

**Next session: 5 retests/recall checks due before any new content.**

> 📌 **Retest queue (priority order):**
> 1. **WP002 — due 2026-05-12** *(bash frequency-count discipline; failures = 1, stage 0; **third failure triggers a remediation challenge** — highest-stakes retest. Cross-track signal from session 7 broadens the WP description: same family of habit surfaced again on Evidence Trail Task 4 — trusted file content without inspecting adjacent terminal evidence.)*
> 2. **WP003 — due 2026-05-14** *(concepts phishing analysis; verification-habit on a NEW phishing email — fresh email needed, prepare in advance)*
> 3. **WP004 — due 2026-05-14** *(python file iteration; needs a challenge that exposes a real or simulated large-file scenario so the readlines footgun is visible. **Positive signal from Brute Force Source: lazy iteration used unprompted — prognosis good but still test on a NEW twist.**)*
> 4. **🆕 Redirection recall check — due 2026-05-14** *(forward-looking recall check at user's proactive request, NOT a WP. 4 cold prompts on operator behaviour, no scaffold, no scrollback. Pass = recall confirmed. Fail = formalise as WP.)*
> 5. **WP001 — due 2026-05-15** *(cross-track instruction precision; stage 1 → 2 if pass)*

> 🗺️ **After retests — user picks new content from:**
> - **🆕 Bash L2 #1** — first L2 challenge. Scripting basics (variables, loops, conditionals, exit codes). Lab depends on choice: file organiser/log monitor reuse existing labs; ping sweep needs Metasploitable target.
> - **Python L1 #3** — next Python L1 challenge. Likely socket basics, IP address validator, or password strength evaluator (per CLAUDE.md L1 examples).
> - **Concepts L1 #2** — likely network/CIA reasoning scenario; **still deferred until WP003 retest passes** to avoid stacking.

> 🔧 **Tutor process — confirmed in effect, plus two refinements from session 7:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
> 7. **NEW (2026-05-10):** When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`. Use *"two paths together"* or list with commas. *(From Evidence Trail Task 4 brief defect.)*
> 8. **NEW (2026-05-10):** Never give a working answer and ask the user to "pick" from inside it. Either give the answer cleanly OR show a placeholder for them to fill — not both. *(Restates `precise_meta_comms`; from Python L1 #2 closing-step defect.)*

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried forward from session 6.)*

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — gates Bash L2 ping sweep, most Python L3 work. Consider as a side task if user wants to unblock the broadest L2/L3 paths.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | L1 | ██░░ 2/4 | 2 | 🟢 Active — clean second challenge, scope discipline now a pattern |
| 🖥️ Bash | **L1 ✅** | ████ 4/3 | 4 | **✅ COMPLETE 2026-05-10** — first track to clear L1; ready for L2 |
| 🔐 Concepts | L1 | █░░ 1/3 | 1 | 🟡 Active but deferred — WP003 retest gates next challenge |
| 🎭 Scenarios | — | Locked | 0 | 🔒 Unlocks when all 3 core tracks reach L2 |

**Bash L1 → L2 transition:** Bash track now ready for L2 (scripting basics — variables, loops, conditionals, exit codes). First L2 challenge available next session.

---

## 📝 Session 7 Summary (2026-05-10 — same-day return after Session 6)

### ✅ Side task — `bash-L0-first-footprints` archived

- Filled `<target>` placeholder in Final Solution with `/mnt/d/cybersecurity_learning/`.
- Stripped stale tutor-scaffold hint line that became redundant once "What I Got Wrong First" was filled.
- Wrapped Final Solution in fenced bash block per find-tour convention.
- All 5 generated write-ups now archived; portfolio counter at 5/5 → eventually 7/7 after this session's archives.

### ✅ Bash L1 — Evidence Trail (closes the level)

- **Four-task redirection challenge** covering all four operators (`>`, `>>`, `2>`, `> file 2>&1`) against `labs/bash-L1/triage/`.
- **All 4 tasks correct** against pre-verified expected outputs. Tasks 1-3 zero hints. Task 4 needed Tier 1 REFRAME after a tutor-side brief-wording defect (capital "AND" in "BOTH X AND Y" clashed with shell `&&` — 3 failed `find . && /nonexistent_path` attempts before reframe).
- **Strong points:** Task 4 redirection-operator order right first time (`> file 2>&1`, not the broken `2>&1 > file` reversal); ran unredirected `cat var/log/syslog.99` first to observe natural error before redirecting (verify-before-commit instinct, unprompted); cleaned up stray `file` artifact without re-prompting; unstuck via single Tier 1 reframe with no further escalation.
- **Weakness flagged (no new WP):** failed Task 4 attempts each printed `find .` output to terminal — hard evidence the `&&` was splitting the command — not noticed before reframe. **Same family as WP002** (trust visible output without inspecting adjacent evidence). Cross-track evidence note added to WP002 description.
- **Bash L1 COMPLETE** — first track to clear L1. Checkpoint logged.

### ✅ Python L1 #2 — Brute Force Source (`ip_extractor.py`)

- **One new concept:** `str.split()` + indexed list access. 4-line script, scope discipline held again — now a pattern, not a fluke.
- **Output:** 27 IPs in file order, exact match against pre-verified reference. Diff empty.
- **Three positive signals:**
  1. **WP004 reinforcement landed unprompted** — `for line in f:` directly used, no `f.readlines()` reach despite the WP being only 4 hours old.
  2. **WP002 family trap avoided** — Failed-only filter held; Accepted lines correctly skipped despite the simpler-looking path being to skip the filter entirely (which would have produced 3 garbage entries with port numbers as IPs).
  3. **Chose `.split()` over manual char indexing** — token-based abstraction tolerates whitespace variation; handled the *"May  5"* two-space gap silently.
- **Diagnostic shaky-string-handling (2026-04-27 task 3) addressed through application** — same skill as the `admin:password123` split, applied to log lines. No separate drill needed.
- **Cross-track closing step** built into the brief at user's proactive request: *"without practice i will 100% forget"* the redirection operators learned 30 minutes earlier. Closing-step (`python3 ip_extractor.py > python/L1/ips.txt`) reinforces redirection while building the natural Python→Bash workflow real triage scripts use.
- **Tutor-side meta-comms defect:** in the closing-step instructions, gave the working command with `>` pre-filled, then said *"pick the operator yourself"* — contradictory. User flagged it. Restating existing memory (`precise_meta_comms`) — no new memory needed.

### 🆕 Redirection refresher scheduled

User raised a forecasted retention concern (rare and valuable — forecasting forgetting before discovering it on a retest beats the reverse). Recall check scheduled for 2026-05-14 alongside WP003/WP004. Format: 4 cold prompts, no scaffold. Not a WP — forward-looking recall check.

### 🔧 Three new cross-track links logged

Total cross-track connections: **4 → 6**. New entries:
- *Python `.split()[N]` mirrors Bash `awk '{print $N}'`* — same brittleness; same robust fix (regex on value shape, not position).
- *Python script output captured to file via Bash redirection (`>`)* — real triage workflow built into Brute Force Source as closing-step.

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters | 1 | 0 | **2026-05-15** |
| WP002 | bash | Frequency-count pipelines: skips count-column sorting, trusts pipeline output without inspecting intermediate stages. **Generalisation 2026-05-10:** broader pattern is *trust visible output without inspecting adjacent evidence that contradicts the assumption*. | 0 | **1** | **2026-05-12** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step the lens requires (method gap, not knowledge gap) | 0 | 0 | **2026-05-14** |
| WP004 | python | File iteration defaults to `f.readlines()` (eager, full-file load) instead of iterating the file object directly (lazy). Crashes on production-scale logs. **Positive signal 2026-05-10:** lazy iteration used unprompted in Brute Force Source — prognosis good but still test on new twist. | 0 | 0 | **2026-05-14** |

**Cross-track pattern note:** WP002 (bash, skip-the-inspection-step), WP003 (concepts, skip-the-verification-step), and the Evidence Trail Task 4 *not-reading-terminal-as-evidence* incident may all be the same underlying habit — *infer the answer without doing the named verification step / without checking adjacent state*. Three retests in the next 5 days will tell us whether this pattern is persistent or context-bound.

**Retest history:**
- **WP001 (2026-05-08):** ✅ Passed. Brief Precision: 3 sub-tasks, all parameters exactly as briefed, single-tool answers.
- **WP002 (2026-05-08):** ❌ Failed. Frequency Recall: correct answer surfaced but missed `Failed`-only filter and intermediate inspection (both explicit brief criteria).

> ℹ️ **WP002 description history:** earlier evidence of *"`sort -r` would misrank counts ≥10"* was empirically falsified 2026-05-08. The round-1 bug from Trail in the Logs (no count-column sort at all) remains real. The 2026-05-10 generalisation broadens the description beyond frequency-counting.

---

## 👀 Watch-Areas

*None active.* WA002 promoted to WP003 on 2026-05-10. WA001 promoted to WP001 on 2026-04-28.

---

## 📅 Retests + Recall Checks Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **2026-05-12** | WP002 | Retest | bash | 0 | 1 *(third failure → remediation challenge)* |
| **2026-05-14** | WP003 | Retest | concepts | 0 | 0 |
| **2026-05-14** | WP004 | Retest | python | 0 | 0 |
| **2026-05-14** | 🆕 Redirection refresher | Recall check (not WP) | bash | — | — |
| **2026-05-15** | WP001 | Retest | cross-track | 1 → 2 if pass | 0 |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour)*
- [x] **All three core tracks active at L1** *(2026-05-10)*
- [x] **🆕 First track reaches Level 1 complete — Bash L1 ✅** *(2026-05-10 — Evidence Trail closed redirection criterion)*
- [ ] All tracks reach Level 1 complete *(Python 2/4, Concepts 1/3 remaining)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups *(currently 7 — 3 to go)*

---

## 🗺️ Up Next

**Bash (L2):** 🆕 First L2 challenge available — scripting basics (variables, loops, conditionals, exit codes). CLAUDE.md L2 examples: ping sweep (lab-only — gated on Metasploitable install), log monitor, file organiser. Lab choice unblocks specific challenges.
**Python (L1):** Challenge #3 — likely socket basics, IP address validator, or password strength evaluator. Two more L1 challenges to close the level.
**Concepts (L1):** Challenge #2 — network or CIA-triad reasoning. **Still deferred** until WP003 retest passes 2026-05-14.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**6 logged.**

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]`. Bash version is pipe-ready one-shot; Python version composes inside larger scripts.
- *2026-04-28* — **Bash ↔ Python**: frequency analysis. Bash: `... | sort | uniq -c | sort -nr | head`. Python: `Counter(iterable).most_common(N)`. Same gotcha in both: default sort/min/max on numeric strings is lexicographic.
- *2026-04-28* — **Bash ↔ Python**: positional field extraction is fragile. `awk '{print $11}'` and `line.split()[10]` both break when log format shifts. Real fix: regex on value *shape*.
- *2026-05-10* — **Bash ↔ Python**: log line filtering by substring. Bash: `grep "Failed" auth.log`. Python: `with open(path) as f: for line in f: if "Failed" in line: print(line, end="")`. **Asymmetric gotcha:** Python defaults to a `f.readlines()` footgun that Bash `grep` doesn't have because it streams.
- 🆕 *2026-05-10* — **Bash ↔ Python**: positional field extraction via `.split()[N]` mirrors `awk '{print $N}'`. Python's `.split()` with no args matches awk's default whitespace handling — both reward token-based parsing over byte-based parsing. **Brittleness identical**: index points at wrong field if log format shifts.
- 🆕 *2026-05-10* — **Python → Bash**: script output captured to file via Bash redirection (`>`). Real triage workflow — Python script extracts/parses; Bash redirection captures output for handoff. Same `>` vs `>>` decision as Evidence Trail Tasks 1 and 2: overwrite for snapshot data, append for accumulation.

---

## 📈 Weekly Summary

**2026-05-04 → 2026-05-10:** 3 sessions, ~310 minutes total (~**5h 10m**). **5h target hit** — recovery trajectory complete: week-of-2026-04-27 was 70min, week-of-2026-05-04 is 310min. Three challenges completed in this window: Bash L1 Find Tour, Concepts L1 #1, Python L1 #1, Bash L1 Evidence Trail (closes Bash L1), Python L1 #2 — five total.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box).
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**. Required before any scanning / network challenge. Gates Bash L2 ping sweep and most Python L3 work.
- ✅ `labs/bash-L1/triage/` reused 2026-05-10 for Evidence Trail. Lab now contains 3 evidence files (`findings.txt`, `errors.txt`, `full-capture.txt`) from the challenge — these can stay as portfolio artefacts or be cleaned up if the lab needs reset for future use.
- ✅ `labs/bash-L1/retest-wp002/auth-snippet.log` reused 2026-05-10 as data source for Brute Force Source (Python L1 #2). Reusable again for next WP002 retest 2026-05-12.

---

## 📁 Portfolio Stats

- Write-ups generated: **7** *(↑ from 5)*
- Write-ups archived (with reflections filled): **7** *(↑ from 4 — full archive parity, all 7 generated write-ups archived)*
- Total challenges completed: **7** *(↑ from 5)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **7** *(↑ from 6)*
- Total hours: **~7.4** *(↑ from 5.4)*
