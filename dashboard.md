# Cybersecurity Training Dashboard
*Last updated: 2026-05-19 — after Session 14 (WP002 retest r3 — mechanical facet cleared clean third time; verify-don't-proxy facet failed unprompted; user chose strict-bar accounting, failures 2 → 3, WP002 → remediation challenge)*

---

## Pickup Here

**SESSION 15 PRIORITY 1 — design and deliver the WP002 REMEDIATION CHALLENGE.** Failures = 3 (escalated 2026-05-19 after r3 retest). Per CLAUDE.md: small, scaffolded task targeting just the weak point — pass = WP002 mastered. **Scope narrow:** test verify-don't-proxy discipline specifically. **DO NOT re-test mechanical facet** (filter-first + count-sort + no head-truncation — cleared clean three consecutive retests; original 2026-04-28 fingerprint gone). **Format consideration:** prior retests (r1, r2) baked verification into brief as explicit commands (`wc -l`, pre-`head` sorted list); r3 attempted analytical-noticing format without telegraphing the shift — user pushed back, tutor agreed. Remediation must EITHER (a) bake verification commands into brief matching r1/r2 format, OR (b) explicitly telegraph if analytical-noticing format used.

**Session 14 closed 2026-05-19** — 30-min agreed lock, ~50 min wall-clock including pre-session VSCode layout fix. WP002 r3 retest delivered. Mechanical pipeline clean (`grep Failed | awk '{print $13}' | sort | uniq -c | sort -nr | head -5` → matched tutor-key exactly). Verify-don't-proxy facet needed one Tier 1 reframe before user surfaced the dual-role IP (198.51.100.73 → jenkins credential compromise). User pushed back on the format-shift goalpost; tutor agreed, offered split / partial-pass / full-pass options. User chose strict-bar accounting. No write-up — retest session.

> **Retest queue (priority order):**
> 1. **WP002 — AWAITING REMEDIATION CHALLENGE** *(failures = 3; next session item 1)*
> 2. **WP004 — due 2026-05-22** *(python file iteration; stage 1; one more clean retest = mastered)*
> 3. **WP005 — due 2026-05-22** *(concepts vuln triage / version-check; stage 0; first retest)*
> 4. **WP003 — due 2026-05-23** *(concepts phishing analysis; stage 1; one more clean retest = stage 2)*
> 5. **WP001 — due 2026-05-29** *(cross-track instruction precision; stage 2; one more clean retest = mastered)*

> **New content options (after the WP002 remediation):**
> - **Bash L2 #1** — scripting basics (variables, loops, conditionals, exit codes). awk syntax revisit fits here too (untouched four sessions running).
> - **Python L2 #1** — tool-building (subprocess, argparse, pipe-friendly output). Port scanner.
> - **Concepts L2 #1** — vulnerability classes / attack methodologies / defence frameworks. Map to TM256.

> **Tutor process — in effect:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried in Constraints.
> 5. When introducing analysis frameworks, state explicitly *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
> 7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`.
> 8. Never give a working answer and ask the user to "pick" from inside it.
> 9. When a Tier 1 reframe gets shortcut, do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction.
> 10. Brief-precision miss recurs when concrete deliverables are implicit. Count concrete deliverables explicitly. **VALIDATED 2026-05-15.**
> 11. Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic.
> 12. Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1).
> 13. **Phishing-analysis retests test verification habit specifically when the email contains at least one lens-indicator the analyst cannot resolve from email content alone.** **VALIDATED 2026-05-16. GENERALISED 2026-05-18.**
> 14. *(Forming.)* When external-learning entries are noted but flagged "not sure why this matters", schedule a teach-first slot before any application slot. Origin: session 12 design-defect.
> 15. **Brief precision applies to the tutor as much as the user.** Every grading criterion must trace back to a property explicitly stated in the brief. **Origin 2026-05-18.**
> 16. **NEW 2026-05-19 — When retesting a cross-track-generalised weak point in a DIFFERENT brief format than prior retests, the new format must be telegraphed in the brief.** Otherwise the unprompted-discipline bar is unfair — the user is being asked to spontaneously demonstrate a discipline in a shape they've never been tested on. **Origin:** WP002 r3 — verify-don't-proxy facet has been in scope since 2026-05-10's cross-track generalisation, and r2 (2026-05-15) had the same dual-role IP trap. But r1/r2 baked verification into briefs as explicit commands; r3 expected analytical noticing of an in-log fact. User pushed back on the format shift; tutor owned it in-session. **How to apply:** if a retest format diverges from prior retests on the same WP, state the format change in the brief OR retain prior format. Sibling to note 10 (count concrete deliverables) and note 15 (grading criteria traceable to brief properties).

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried since session 6.)*
- External courses budget decision — user has TryHackMe subscription unused.
- Redirection `<` operator: user reports never trained; introduce as new content OR amend the session-10 recall check to drop Q4.

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — highest-leverage side task to unblock the broadest L2/L3 paths.

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L1 OK** | ████ 4/4 | 4 | **COMPLETE** — ready for L2; WP004 retest passed 2026-05-15, stage 1 |
| Bash | **L1 OK** | ████ 4/3 | 4 | **COMPLETE** — ready for L2; WP002 awaiting remediation challenge |
| Concepts | **L1 OK** | ████ 3/3 | 3 | **COMPLETE 2026-05-18** — ready for L2 |
| Scenarios | — | Locked | 0 | Unlocks when all 3 core tracks reach L2 |

---

## Session 14 Summary (2026-05-19 — 30-min agreed, ~50 min wall-clock)

### Challenge run

**WP002 retest r3** — third attempt. Fresh 30-line SSH auth log at `labs/bash-L1/retest-wp002-r3/auth-snippet.log`, new IPs/usernames/counts vs r2 to prevent pattern-matching. Brief asked for top 5 external IPs by failed-login count, with an explicit "if something warrants a follow-up note, write it" hook for the verify-don't-proxy facet.

### What cleared clean

User's pipeline: `grep 'Failed' auth-snippet.log | awk '{print $13}' | sort | uniq -c | sort -nr | head -5`

Output matched tutor-key exactly. Top 5: 203.0.113.62(7), 198.51.100.73(6), 192.0.2.144(4), 172.105.92.18(3), 91.218.114.31(2). **Mechanical facet — third consecutive clean execution.** Original 2026-04-28 WP002 fingerprint (no count-sort, alphabetical truncation via `head` before `sort -nr`) is gone.

### What didn't fire

First submission was pipeline + output only — no follow-up note. The dual-role IP trap (198.51.100.73 also has 3 Accepted/jenkins logins in the same file) went unsurfaced. Tier 1 reframe delivered: *"grep each top-5 IP — are ALL its lines `Failed`?"* — landed cleanly. User identified the jenkins credential compromise and the SOC-action implication accurately and sharply (block-5 wastes resources; rotate jenkins creds + audit jenkins activity since 03:14:58 is the real response).

### Tutor error owned in-session

**Format shift not telegraphed.** Prior retests (r1 2026-05-08, r2 2026-05-15) baked verification into the brief as explicit commands — *"run `wc -l` on the filter stage"*, *"check the pre-`head` sorted list before stating the answer."* r3 attempted a different format: analytical noticing of an in-log fact. User pushed back: "all the other attempts have been focusing on the bash commands, nothing to do with read the log and figure that out, surely that would be more a concepts task? I feel like you moved the goalposts."

Tutor verified against `progress.json`:
- WP002 canonical description includes verify-don't-proxy generalisation since 2026-05-10. *Concept* in scope.
- r2 (2026-05-15) also had a dual-role IP trap (185.220.101.50). *Trap design* consistent.
- BUT r1/r2 baked verification into the brief as explicit commands; r3 expected spontaneous analytical noticing. *Format shifted, not telegraphed.*

Owned in-session. Process note 16 promoted.

### User's call — strict-bar accounting

Tutor offered three options after owning the format-shift: full pass (fair given the shift), partial pass with WP002 split into WP002a (mechanical, cleared) + WP002b (verify-don't-proxy, active), or strict-bar full fail. User chose strict-bar:

> *"listen im fine with you putting the failure counter at 3 and then me having to do something about it"*

This is the WP003 verify-don't-proxy discipline applied to tutor evaluation, generalising further outward — now into self-assessment. User declined the softer option even when offered. Recorded as positive signal. The remediation challenge consequence is the structured escape hatch, not a punishment.

### Hint tier log

Tier 1 — one reframe. Delivered clean, landed clean.

### Pushback as positive signal — now three consecutive sessions

| Session | Pushback target |
|---------|----------------|
| 12 | Pushed back on FLT Evidence A "no MD5" conclusion path; led to Evidence B sandbox-first reasoning |
| 13 | Pushed back on TLB file-server CIA-primary critique; tutor withdrew point (process note 15) |
| 14 | Pushed back on WP002 r3 format-shift goalpost; tutor agreed, process note 16 promoted; user then chose stricter accounting than tutor offered |

Discipline generalising in the right direction. Treat future pushback as signal, not deflection.

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. 2026-05-15 retest clean. | 2 | 0 | **2026-05-29** |
| WP002 | bash | Frequency-count pipelines + verify-don't-proxy generalisation. **MECHANICAL FACET CLEARED** (third clean execution 2026-05-19). **VERIFY-DON'T-PROXY FACET** — needs unprompted-on-first-submission demonstration. | 0 | **3** | **AWAITING REMEDIATION** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing the verification step. 2026-05-16 retest PASSED unprompted. | 1 | 0 | **2026-05-23** |
| WP004 | python | File iteration defaults to `f.readlines()` instead of `for line in f:`. 2026-05-15 retest PASSED. | 1 | 0 | **2026-05-22** |
| WP005 | concepts | Vulnerability triage skips version-check step before deciding response. 2026-05-18 first-pass missed entirely. | 0 | 0 | **2026-05-22** |

**Retest history (most recent):**
- **WP002 (2026-05-19):** ❌ FAILED on verify-don't-proxy facet. Mechanical pipeline clean. Format-shift owned by tutor; user chose strict-bar accounting. Failures 2 → 3. **WP002 → remediation challenge.**
- **WP003 (2026-05-16):** ✅ PASSED. Fresh HMRC phishing, verification habit unprompted. Stage 0 → 1.
- **WP001 (2026-05-15):** ✅ PASSED. Multi-sub-task brief, no nudges. Stage 1 → 2.
- **WP002 (2026-05-15):** ❌ FAILED. Same fingerprint as 2026-05-08. Failures 1 → 2.
- **WP004 (2026-05-15):** ✅ PASSED. Lazy iteration unprompted. Stage 0 → 1.

---

## Watch-Areas

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable. Untouched sessions 11, 12, 13, 14. Fits naturally with the WP002 remediation if it uses bash.

---

## Retests + Remediation Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **Session 15 (next)** | WP002 | **Remediation Challenge** | bash | 0 | 3 *(pass = mastered)* |
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
- [x] **Second track reaches Level 1 complete — Python L1** *(2026-05-11)*
- [x] **🏆 ALL TRACKS REACH LEVEL 1 COMPLETE** *(2026-05-18)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [x] **Portfolio has 10+ archived write-ups** *(2026-05-18 — 11 total)*

---

## Up Next

**Next session:** WP002 remediation challenge — scope-narrow, verify-don't-proxy only, mechanical facet NOT re-tested.
**Concepts (L2):** Available; entry pace may not need scaffolding.
**Bash (L2):** Available — scripting basics. awk-syntax revisit pairs naturally.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** Locked until all three tracks at L2.

---

## Cross-Track Connections

**7 logged.** *(Unchanged — Session 14 was retest, no new tooling-equivalence link surfaced.)*

---

## Weekly Summary

**2026-05-08 → 2026-05-15 (last regen):** 4 sessions, ~370 minutes (~**6h 10m**). Within 5–10h target.
**Running total 2026-05-15 → 2026-05-19:** 3 sessions (12, 13, 14), ~115 minutes (~**1h 55m**) — early-week pace.
**Next formal weekly summary regenerates 2026-05-22.**

---

## Lab Status

- Ubuntu VM running (host attacker box).
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**.
- `labs/bash-L1/triage/` — reusable.
- `labs/bash-L1/retest-wp002/` — retired (r1, 2026-05-08).
- `labs/bash-L1/retest-wp002-r2/` — retired (r2, 2026-05-15).
- `labs/bash-L1/retest-wp002-r3/` — used 2026-05-19 (r3). **Retain for now** — may inform remediation challenge design.
- `python/L1/` — five scripts.
- `concepts-track/L1/` — `challenge-2-brief.md` (First Light Triage brief).
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target.

---

## Portfolio Stats

- Write-ups generated: **11** *(unchanged — Session 14 was retest)*
- Write-ups archived: **11**
- Total challenges completed: **11**
- Total challenges attempted-unfinished: 2
- Total sessions: **14** *(↑ from 13)*
- Total hours: **~12.8** *(↑ from 12.0 — Session 14 ran ~50 min wall-clock)*
