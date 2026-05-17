# Cybersecurity Training Dashboard
*Last updated: 2026-05-18 — after Session 12 (Concepts L1 #2 First Light Triage complete with revision; WP005 logged; write-up filled, cleanup-passed, archived)*

---

## Pickup Here

**SESSION 13 NEXT — WP002 retest is TOMORROW (2026-05-19) and is the highest-stakes item on the board.** Failures = 2; one more failure triggers a remediation challenge. Design as a fresh bash frequency-count with the **retest-wp002-r3** dataset (generate before session). The verify-don't-proxy discipline must fire **unprompted** on first submission.

**Session 12 write-up archived 2026-05-18** — [writeups/concepts-L1-first-light-triage-2026-05-18.md](writeups/concepts-L1-first-light-triage-2026-05-18.md). Wrap-publish flow ran end-to-end (cleanup pass → archive → stage → commit → push). Portfolio now at **10 archived write-ups** — checkpoint hit.

> **Retest queue (priority order):**
> 1. **WP002 — due 2026-05-19 TOMORROW** *(bash frequency-count discipline; failures = 2, stage 0; **next failure = remediation challenge** — highest-stakes retest)*
> 2. **WP004 — due 2026-05-22** *(python file iteration; stage 1; one more clean retest = mastered)*
> 3. **WP005 — due 2026-05-22 NEW** *(concepts vuln triage / version-check before action; stage 0; first retest checks if NVD-first habit fires unprompted)*
> 4. **WP003 — due 2026-05-23** *(concepts phishing analysis; stage 1; one more clean retest = stage 2)*
> 5. **WP001 — due 2026-05-29** *(cross-track instruction precision; stage 2; one more clean retest = mastered)*

> **New content options for sessions beyond the WP002 retest:**
> - **Bash L2 #1** — scripting basics (variables, loops, conditionals, exit codes). File organiser / log monitor reuse existing labs; ping sweep needs Metasploitable.
> - **Python L2 #1** — tool-building (subprocess, argparse, pipe-friendly output). Port scanner scales First Knock primitive across a range with concurrency.
> - **Concepts L1 #3** — last one to close Concepts L1 (third-of-three core tracks pending). Open topic. Possible angles: applied attack-tree reasoning; defender-roles scenario; OR a cross-track tooling concept now that WP005 is fresh and OSINT material is loaded.

> **Spaced-repetition flag (carried forward, untouched two sessions running):**
> - **awk action-block syntax** — third L0/L1 exposure on session 10 still needed full T1→T2→T3 escalation; user reports "awk just doesn't sit in my mind". Treat as syntax-recall gap, not conceptual. Schedule a short revisit alongside next bash work.

> **Tutor process — confirmed in effect:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
> 7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`.
> 8. Never give a working answer and ask the user to "pick" from inside it.
> 9. When a Tier 1 reframe gets shortcut, do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction.
> 10. Brief-precision miss recurs when concrete deliverables are implicit. Count concrete deliverables explicitly. **VALIDATED 2026-05-15.**
> 11. Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic.
> 12. Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1).
> 13. **Phishing-analysis retests test verification habit specifically when the email contains at least one lens-indicator the analyst cannot resolve from email content alone.** **VALIDATED 2026-05-16.** **GENERALISED 2026-05-18** — same principle applied to Evidence C of First Light Triage (the affected-or-not status was not resolvable from ticket text alone); trap fired, gap surfaced, WP005 logged.
> 14. **(Forming, not yet formal.)** When external-learning entries are noted but flagged "not sure why this matters", do NOT assume the next challenge can run without re-teaching — schedule a teach-first slot before the application slot. Origin: session 12 design-defect where the brief assumed THM retention had filled the OSINT-tools prerequisite; user opened by naming the gap; session pivoted to teach-first-then-apply within the same slot.

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried since session 6.)*
- External courses budget decision — user has TryHackMe subscription unused.
- Redirection `<` operator: user reports never trained; introduce as new content in a future bash session, OR amend the session-10 recall check to drop Q4.

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — highest-leverage side task to unblock the broadest L2/L3 paths.

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L1 OK** | ████ 4/4 | 4 | **COMPLETE** — ready for L2; WP004 retest passed 2026-05-15, stage 1 |
| Bash | **L1 OK** | ████ 4/3 | 4 | **COMPLETE** — ready for L2 |
| Concepts | L1 | ██░ 2/3 | 2 | Active — First Light Triage complete 2026-05-18, **L1 #3 will close the level** |
| Scenarios | — | Locked | 0 | Unlocks when all 3 core tracks reach L2 |

---

## Session 12 Summary (2026-05-18 — 30-min planned, ~35-min actual, slight over-run)

### Challenge run

**Concepts L1 #2 First Light Triage** — OSINT / threat-intel source selection scenario. 3-evidence SOC-triage (brute-force IP, suspicious file hash, CVE alongside framework). Closes the THM unresolved entry on shodan/censys/virustotal/exploit-database.

### Session-design pivot at start

Brief had "no web lookups" constraint assuming THM retention had filled the prerequisite. **User opened by naming the gap honestly:** *"the no web lookups constraint makes this task almost obsolete for me as i dont remember at all what each threat-intel source does."* Tutor owned the design defect (CLAUDE.md "why before what" rule skipped; one THM exposure ≠ retention). Session pivoted to **teach-first-then-apply** within the same 30-min slot:
- ~5 min tutored intro on the 4 sources with citation links + NVD/MITRE sister-tool flag for CVE-detail work.
- ~15 min triage application with intro available as reference.
- ~10 min review.

### Per-evidence results

- **Evidence A (Shodan / brute-force IP):** Spontaneously named Censys as alternative inside 15 min of first hearing the name — double-exposure → application working as designed. Decision shape right (Shodan → block). 🟡 Phrased Shodan as returning *verdicts* rather than *data* — taught with banner-profile decision ladder (commodity scanner / residential ISP / cloud range / nothing exposed).
- **Evidence B (VirusTotal / file hash):** Cleanest answer of the three. Addressed BOTH positive and negative cases. **Specifically good:** the negative-case action (*sandbox first, then submit to VT*) is the SOC analyst pattern — L2/L3 territory, not L1. Most learners stop at the positive case. 🟢 Minor wording miss (file already quarantined; "don't download" is wrong pivot — should be "confirm containment + check delivery chain"). VirusTotal upload-disclosure caveat taught as security implication.
- **Evidence C (Exploit-DB / CVE):** Jumped straight from "CVE mentioned alongside framework" to "halt any app, remove the framework". Skipped the version-check step. 🔴 Critical — *is our deployed version even affected?* is the question that has to come first. 🔴 Critical — emergency shutdown stated as only option, missed the **patch → vendor mitigation → compensating control → emergency shutdown** ladder. **WP005 logged.**

### Revision on Evidence C

Verification CONCEPT landed (*"we can find out if we are actually vulnerable"*) but tool detail still wrong (kept exploit-db instead of NVD for the version-check). NVD vs exploit-db split re-taught: NVD answers *"am I vulnerable"* (returns affected version range); exploit-db answers *"how urgent"* (does public PoC exist). Two tools, two questions, NVD first. User then asked honestly what *vendor mitigation* and *compensating control* meant — defined both with concrete examples.

### Honesty discipline — three instances in one session

Each is the WP003 corrective behaviour (name the verification, don't substitute confidence) applied to the user's own knowledge state:
1. **Session-open admission** that the OSINT tools weren't retained — caught a tutor design defect.
2. **Revision framing** that let errors surface fast instead of being papered over.
3. **Explicit question** on the unfamiliar ladder terms (vendor mitigation, compensating control) — declined to pattern-match through them.

Strong positive signal — the discipline being drilled on phishing analysis is generalising to honest self-reporting in any context, which is the load-bearing skill behind the spaced-repetition system actually working.

### Key process observation

**Process note 13 generalised.** The phishing-retest design principle (scenario must contain at least one indicator the analyst cannot resolve from the evidence alone) transfers cleanly to vuln-triage scenarios. Evidence C's *"on-call did not say whether your deployed version is affected"* was the verify-or-skip trap; it fired correctly and surfaced the WP005 gap. The trap design template now has cross-domain validation.

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. 2026-05-15 retest clean pass on explicitly-enumerated brief. | 2 | 0 | **2026-05-29** |
| WP002 | bash | Frequency-count pipelines / verify-don't-proxy generalisation: trust visible output without inspecting adjacent evidence. 2026-05-15 retest FAILED. | 0 | **2** | **2026-05-19 ⚠️** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step. 2026-05-16 retest PASSED unprompted on trap lenses. | 1 | 0 | **2026-05-23** |
| WP004 | python | File iteration defaults to `f.readlines()` instead of `for line in f:`. 2026-05-15 retest PASSED. | 1 | 0 | **2026-05-22** |
| WP005 | concepts | **NEW.** Vulnerability triage skips version-check step before deciding response. Pattern: framework name appears alongside CVE → assumes affected → jumps to action, without naming NVD / vendor-advisory lookup. 2026-05-18 first-pass missed entirely; revision passed concept but kept wrong tool (exploit-db, not NVD). | 0 | 0 | **2026-05-22** |

**Cross-track pattern note — UPDATED 2026-05-18.** WP002 (bash frequency-count), WP003 (concepts phishing analysis), and WP005 (concepts vuln triage) are now **three concrete instances of the same underlying habit — *skip the named verification step* — in three different domains.** The underlying habit is clearly the load-bearing weakness, not any domain-specific knowledge gap. WP003's 2026-05-16 pass remains the positive datapoint on the family; WP002's 2026-05-19 retest is the highest-stakes test of whether the habit is generalising in the right direction.

**Retest history (most recent):**
- **WP003 (2026-05-16):** ✅ PASSED. Fresh HMRC phishing, verification habit unprompted. Stage 0 → 1.
- **WP001 (2026-05-15):** ✅ PASSED. Multi-sub-task brief, no nudges. Stage 1 → 2.
- **WP002 (2026-05-15):** ❌ FAILED. Same fingerprint as 2026-05-08. Failures 1 → 2.
- **WP004 (2026-05-15):** ✅ PASSED. Lazy iteration unprompted. Stage 0 → 1.

---

## Watch-Areas

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable. Untouched sessions 11 and 12.

---

## Retests + Recall Checks Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **2026-05-19 ⚠️** | WP002 | Retest | bash | 0 | 2 *(next failure → remediation challenge)* |
| **2026-05-22** | WP004 | Retest | python | 1 | 0 |
| **2026-05-22** | WP005 | Retest **(first)** | concepts | 0 | 0 |
| **2026-05-23** | WP003 | Retest | concepts | 1 | 0 |
| **2026-05-29** | WP001 | Retest | cross-track | 2 → mastered if pass | 0 |

---

## Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour)*
- [x] **All three core tracks active at L1** *(2026-05-10)*
- [x] **First track reaches Level 1 complete — Bash L1** *(2026-05-10)*
- [x] **Second track reaches Level 1 complete — Python L1** *(2026-05-11; WP004 retest passed 2026-05-15 confirms)*
- [ ] All tracks reach Level 1 complete *(Concepts 2/3 — one more challenge closes L1)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [x] **Portfolio has 10+ archived write-ups** *(2026-05-18 — First Light Triage archived; 10 total)*

---

## Up Next

**Tomorrow (2026-05-19):** WP002 retest — highest-stakes item on the board.
**Concepts (L1):** L1 #3 to close the level. Topic open.
**Bash (L2):** Available — scripting basics. Awk-syntax revisit fits here too.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** Locked.

---

## Cross-Track Connections

**7 logged.** *(Unchanged — Session 12 was reasoning-based, no new tooling-equivalence link surfaced.)*

---

## Weekly Summary

**2026-05-08 → 2026-05-15 (last regen):** 4 sessions, ~370 minutes total (~**6h 10m**). Within 5–10h target. Both Bash L1 and Python L1 closed in this period. **Next formal weekly summary regenerates 2026-05-22.**

---

## Lab Status

- Ubuntu VM running (host attacker box).
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**. Highest-leverage side task.
- `labs/bash-L1/triage/` — reusable.
- `labs/bash-L1/retest-wp002/` — retired (used 2026-05-08; r2 set replaces).
- `labs/bash-L1/retest-wp002-r2/` — built 2026-05-15. **For 2026-05-19 WP002 retest: generate retest-wp002-r3 to prevent pattern-matching, or reuse r2 if pattern-matching is no longer a concern.**
- `python/L1/` — five scripts: `log_filter.py`, `ip_extractor.py`, `password_audit.py`, `port_check.py`, `retest_wp004.py`.
- `concepts-track/L1/` — `challenge-2-brief.md` (First Light Triage brief, kept for retest reference).
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target.

---

## Portfolio Stats

- Write-ups generated: **10** *(↑ from 9 — First Light Triage)*
- Write-ups archived: **10** *(↑ from 9 — First Light Triage filled, cleanup-passed, archived; portfolio 10+ checkpoint hit)*
- Total challenges completed: **10** *(↑ from 9)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **12** *(↑ from 11)*
- Total hours: **~11.5** *(↑ from 10.9)*
