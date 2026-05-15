# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-05-15 — after Session 10 (retest-dense session: WP001 passed → stage 2; WP002 failed → failures 2; WP004 passed → stage 1; redirection recall 2.5/4; WP003 deferred)*

---

## 🎯 Pickup Here

**Next session: WP003 retest FIRST** (overdue since 2026-05-14, slipped from this session due to time pressure). Phishing analysis on a **NEW** email — verification-habit under no-redo-pressure conditions. **Prep the fresh phishing email before the session.**

**🚨 WP002 is now at failures = 2.** Next retest 2026-05-19. **One more failure = remediation challenge.**

> 📌 **Retest queue (priority order):**
> 1. **WP003 — overdue (was due 2026-05-14)** *(concepts phishing analysis; verification-habit on a NEW email; needs fresh email prep)*
> 2. **WP002 — due 2026-05-19** *(bash frequency-count discipline; failures = 2, stage 0; **next failure = remediation challenge** — highest-stakes retest)*
> 3. **WP004 — due 2026-05-22** *(python file iteration; stage 1; one more clean retest = mastered)*
> 4. **WP001 — due 2026-05-29** *(cross-track instruction precision; stage 2; one more clean retest = mastered)*

> 🗺️ **After retests — user picks new content from:**
> - **Bash L2 #1** — scripting basics (variables, loops, conditionals, exit codes). Lab depends on choice: file organiser/log monitor reuse existing labs; ping sweep needs Metasploitable target.
> - **Python L2 #1** — tool-building (subprocess, argparse, pipe-friendly output). Port scanner scales First Knock primitive across a range with concurrency; subdomain enumerator, log anomaly detector, hash identifier are alternatives.
> - **Concepts L1 #2** — likely network/CIA reasoning scenario; **still deferred until WP003 retest passes.**

> 🔁 **Spaced-repetition flag (new):**
> - **awk action-block syntax** — third L0/L1 exposure 2026-05-15 needed full T1→T2→T3 escalation; user reports "awk just doesn't sit in my mind". Treat as syntax-recall gap (like redirection operators), not conceptual. Schedule a short revisit alongside next bash work.

> 🔧 **Tutor process — confirmed in effect:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
> 7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`. Use *"two paths together"* or list with commas.
> 8. Never give a working answer and ask the user to "pick" from inside it. Either give the answer cleanly OR show a placeholder for them to fill — not both.
> 9. When a Tier 1 reframe gets shortcut (user takes the easier step and stops), do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction.
> 10. **Brief-precision miss recurs when concrete deliverables are implicit.** When designing briefs, count concrete deliverables explicitly (e.g. "two test cases — both must be exercised"); don't bury the "all of them" requirement in narrative. **VALIDATED 2026-05-15** — dedicated WP001 retest (4 sub-tasks A/B/C/D, explicitly enumerated) passed clean; two same-session briefs with implicit enumeration produced soft WP001 misses.
> 11. Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic.
> 12. Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1; target must be own machine / own VM / written-authorisation lab). Restate in shorter form at start of each subsequent network challenge.

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried forward from session 6.)*
- External courses budget decision — user has TryHackMe subscription unused.
- THM unresolved entry: shodan/censys/virustotal/exploit database — user flagged "not too sure why they are important" on 2026/05/11. Candidate for Concepts L1 #2 placement after WP003 clears.
- Redirection `<` operator: user reports never trained; introduce as new content in a future bash session, OR amend the recall check to drop Q4.

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — highest-leverage side task to unblock the broadest L2/L3 paths.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | **L1 ✅** | ████ 4/4 | 4 | **✅ COMPLETE** — ready for L2; WP004 retest passed 2026-05-15, stage 1 |
| 🖥️ Bash | **L1 ✅** | ████ 4/3 | 4 | **✅ COMPLETE** — ready for L2 |
| 🔐 Concepts | L1 | █░░ 1/3 | 1 | 🟡 Active but deferred — WP003 retest overdue, gates next challenge |
| 🎭 Scenarios | — | Locked | 0 | 🔒 Unlocks when all 3 core tracks reach L2 |

---

## 📝 Session 10 Summary (2026-05-15 — 60-min planned, ~70-min actual)

### Retests run

**WP001 ✅ PASSED — Multi-Sub-Task Brief Precision (4 sub-tasks A/B/C/D).** All four sub-tasks delivered first pass, zero nudges. Task B trap (Accepted line at file position 29 between Failed lines) avoided correctly — user wrote `grep 'Failed' | tail -3` rather than `tail -3` of the whole file. Output-type discipline held: numbers where briefed, IPs without counts where briefed. **Stage 1 → 2.** Validates process note 10. Next retest 2026-05-29 (one more clean = mastered).

**WP002 ❌ FAILED — Failed-Login Frequency Audit (Retest r2).** First submission: pipeline construction correct, top IP identified correctly (45.142.122.81 = 12), but ran zero of two brief-required verification checks AND used `head -1` not `head -5`. **Same fingerprint as 2026-05-08 retest** — correct answer surfaces; verification discipline does NOT fire unprompted. Revision was clean once gaps were named in review. Awk action-block syntax recall needed full T1→T2→T3 escalation. **Failures 1 → 2. Stage stays 0. Next retest 2026-05-19. ONE MORE FAILURE = REMEDIATION CHALLENGE.**

**WP004 ✅ PASSED — Distinct Invalid Users.** `for line in f:` reached for unprompted on first submission. **Lazy iteration discipline held under fatigue, Windows-path friction, and visible frustration — strongest positive signal of the session.** First submission counted distinct source IPs (4) instead of distinct usernames (5) — WP001 family wrong-question miss; revised cleanly. **Stage 0 → 1.** Next retest 2026-05-22.

### Recall checks run

**Redirection recall — 2.5/4.** `>` and `>>` clean; `2>` partial (missed that unredirected stdout still goes to terminal); `<` blank — user reports never trained. Q4 likely out-of-scope on tutor's part; needs follow-up.

### Deferred

**WP003 retest deferred** — was already 1 day overdue today; rolled forward to next session as first priority. Retest_due unchanged at 2026-05-14 (overdue date preserved as truth).

### Key process observations

- **Enumeration discipline closes WP001.** Clean retest pass on explicitly-enumerated brief; two soft misses on same-session briefs with implicit enumeration. The contrast is the signal.
- **Awk syntax recall is not durable.** Third L0/L1 exposure, full T1→T2→T3 escalation needed. Flagged for spaced-repetition revisit.
- **Honest gap reports from user three times this session** ("awk just doesn't sit in my mind", "the man page makes 0 sense to me", "i dont remember learning this one"). Strong process signal — honest reporting is exactly what makes the spaced-repetition system work.

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. **2026-05-15 retest CLEAN PASS** on explicitly-enumerated brief; same session showed two soft misses on briefs with implicit enumeration. Stage 1 → 2. | 2 | 0 | **2026-05-29** |
| WP002 | bash | Frequency-count pipelines / verify-don't-proxy generalisation: trust visible output without inspecting adjacent evidence. **2026-05-15 retest FAILED** — same fingerprint as 2026-05-08 (correct top answer surfaces, verification not run unprompted). Four cross-language data points now. | 0 | **2** | **2026-05-19** ⚠️ |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step (method gap, not knowledge gap). **2026-05-15 retest DEFERRED** — needs fresh email prep. | 0 | 0 | **2026-05-14 (OVERDUE)** |
| WP004 | python | File iteration defaults to `f.readlines()` instead of `for line in f:`. **2026-05-15 retest PASSED** — lazy iteration unprompted on first submission, held under fatigue + frustration. Stage 0 → 1. | 1 | 0 | **2026-05-22** |

**Cross-track pattern note:** WP002 (skip-the-inspection-step) and the cross-language data points (use-a-cheap-proxy-instead-of-the-real-test; generalise-from-one-observation; skip-the-named-verification-step) are the same underlying habit. Today's WP002 retest added a fourth instance. Trajectory: NOT yet durably internalised — fires when prompted, not unprompted. Remediation challenge is one failure away.

**Retest history (most recent):**
- **WP001 (2026-05-15):** ✅ PASSED. Multi-sub-task brief, 4/4 sub-tasks first pass, no nudges. Stage 1 → 2.
- **WP002 (2026-05-15):** ❌ FAILED. Same fingerprint as 2026-05-08 (correct answer, no verification). Failures 1 → 2.
- **WP004 (2026-05-15):** ✅ PASSED. Lazy iteration unprompted. Stage 0 → 1.

---

## 👀 Watch-Areas

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable.

---

## 📅 Retests + Recall Checks Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **2026-05-14** ⚠️ | WP003 | Retest (OVERDUE) | concepts | 0 | 0 |
| **2026-05-19** | WP002 | Retest | bash | 0 | 2 *(next failure → remediation challenge)* |
| **2026-05-22** | WP004 | Retest | python | 1 | 0 |
| **2026-05-29** | WP001 | Retest | cross-track | 2 → mastered if pass | 0 |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour)*
- [x] **All three core tracks active at L1** *(2026-05-10)*
- [x] **First track reaches Level 1 complete — Bash L1 ✅** *(2026-05-10)*
- [x] **Second track reaches Level 1 complete — Python L1 ✅** *(2026-05-11; WP004 retest passed 2026-05-15 confirms)*
- [ ] All tracks reach Level 1 complete *(Concepts 1/3 remaining)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups *(currently 9 — 1 to go)*

---

## 🗺️ Up Next

**Concepts (L1):** WP003 retest FIRST (overdue) — fresh phishing email, no scaffold. Then Challenge #2.
**Bash (L2):** Available — scripting basics. Awk-syntax revisit fits here too.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** 🔒 Locked.

---

## 🔗 Cross-Track Connections

**7 logged.** *(Unchanged — no new content session.)*

---

## 📈 Weekly Summary

**2026-05-08 → 2026-05-15 (rolling 7-day):** 4 sessions (sessions 7, 8, 9, 10), ~370 minutes total (~**6h 10m**). Within 5–10h target. Composition: 3 challenges completed (Evidence Trail closes Bash L1, Password Auditor, First Knock closes Python L1), 1 retest-dense closeout (session 10 — 3 retests scored + 1 recall check). Both Bash L1 and Python L1 closed this period. Trajectory healthy. Next formal weekly summary regenerates 2026-05-22.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box).
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**. Highest-leverage side task.
- ✅ `labs/bash-L1/triage/` — reusable.
- ✅ `labs/bash-L1/retest-wp002/` — retired (used 2026-05-08; r2 set replaces for future retests).
- ✅ **`labs/bash-L1/retest-wp002-r2/`** — fresh 2026-05-15. 30 lines, 28 Failed + 2 Accepted, top IP 45.142.122.81 (12). Filter trap on 185.220.101.50 (in BOTH columns; brute-force-then-success IOC pattern). 5 distinct invalid usernames. Reusable for 2026-05-19 WP002 retest IF pattern-matching not a concern; otherwise generate r3.
- ✅ `python/L1/` — contains five scripts now: `log_filter.py`, `ip_extractor.py`, `password_audit.py`, `port_check.py`, `retest_wp004.py`.
- ℹ️ Localhost (`127.0.0.1`) as a fully-legal Python socket test target — pattern established session 9.

---

## 📁 Portfolio Stats

- Write-ups generated: **9** *(unchanged this session — retests don't generate write-ups)*
- Write-ups archived: **9** *(unchanged)*
- Total challenges completed: **9** *(unchanged)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **10** *(↑ from 9)*
- Total hours: **~10.6** *(↑ from 9.4)*
