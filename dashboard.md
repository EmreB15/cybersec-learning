# Cybersecurity Training Dashboard
*Last updated: 2026-05-21 — after Session 15 (WP002 remediation passed → MASTERED; first weak point closed; tutor scope-creep on evaluation owned, process note 17 promoted)*

---

## Pickup Here

**SESSION 16 PRIORITY 1 — WP004 and WP005 retests, both due tomorrow (2026-05-22).**
- **WP004** (python file iteration; stage 1 → mastered if pass). Second clean retest closes the WP. Brief should NOT telegraph the lazy-iteration discipline; the unprompted application is what's marked.
- **WP005** (concepts vuln triage / NVD-first; stage 0 → 1 if pass). First retest since 2026-05-18. Fresh CVE-triage scenario: tests whether NVD-for-version-check fires unprompted before recommending response, and whether response is proportional (patch → vendor mitigation → compensating control → shutdown ladder, not jumping straight to shutdown).
- **WP005 is also the natural watch-home for WA003** (incident-response interpretation, opened session 15). Cadence-reading, action-laddering, and hypothetical-framing of known events to be observed in scoring — but NOT used as scoring criteria unless independently in WP005's described scope. *Process note 17 in effect.*

**Then 2026-05-23:** WP003 retest (concepts phishing; stage 1 → 2 if pass). Can run same day as WP004/WP005 if session budget allows.

**Then new content available:**
- Bash L2 #1 — scripting basics. awk syntax revisit pairs naturally (still untouched five sessions running).
- Python L2 #1 — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
- Concepts L2 #1 — vulnerability classes / attack methodologies / defence frameworks. **Concepts L2 entry pace probably does NOT need scaffolding** — pivot/L2-shape reasoning has now shown reliably at L1 across three consecutive Concepts challenges + WP002 remediation analysis.

**Lab gating:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed.** Blocks broadest L2/L3 paths in both Python and Bash. Localhost (`127.0.0.1`) remains the only legal scanning surface until then.

---

## Session 15 Summary (2026-05-21 — 45-min agreed, ~40 min wall-clock)

### Challenge run

**WP002 Remediation Challenge — Don't Trust the Pipeline** — scoped narrowly to procedural verify-don't-proxy discipline only. Mechanical pipeline given (not in scope). 12-line synthetic SSH auth log at [labs/bash-L1/wp002-remediation/auth-snippet.log](labs/bash-L1/wp002-remediation/auth-snippet.log). Three IPs in pipeline output; strict (a) name verification → (b) run command → (c) conclude order required per IP. Telegraph of analytical-noticing format explicit in brief per process note 16.

### What passed

**The procedural test cleared clean, unprompted.** User wrote *"I am going to use grep here to see what is happening"* **before** running grep, on every IP. Order held: name check → run check → conclude. Exact behavioural reversal of the 2026-05-19 r3 failure (which submitted pipeline+output alone with no follow-up). Zero hint tiers used.

Strong substantive call on 198.51.100.50: user named the **password-spray pattern** from reading the cross-line evidence (4 different usernames from one source = same-password-different-accounts). That is actual SOC terminology, surfacing unprompted at L1.

### Tutor scope-creep error owned in-session

Review extended the marking bar mid-evaluation. The remediation brief was explicitly scoped to *"procedural verify-don't-proxy"* — that bar passed. But review flagged four substantive observations on the 203.0.113.99 (dual-role) analysis as **weaknesses of the remediation**:
1. Hypothetical-framing of the Accepted line ("even if they get it correct" applied to a confirmed Accepted login at 14:30:45).
2. Slow brute-force cadence read as innocuous ("not a threat actor because not few-seconds via script") — but slow-and-low is the more sophisticated rate-limit-evasion pattern.
3. Action-ladder ordering with IP-block as primary, when a confirmed credential success calls for rotate creds → audit session activity → kill active sessions first, with IP block secondary.
4. Summary priority inversion — loud-failed brute-force prioritised over quiet-succeeded brute-force.

All four are **Concepts L2 incident-response interpretation**, not bash WP002 procedural work. User flagged the scope expansion: *"seriously this should be a concepts lab at this point."* Tutor agreed — same fingerprint as session 14's r3 format-shift, but in **evaluation** rather than brief design. Owned in-session.

User also clarified intent on the "even if they get it correct" phrasing (meant: *"block the IP regardless of whether attempt-4 was success or failure"*, not conditional). Point (i) of critique withdrawn under that read.

**Resolution:**
- Substantive observations rehomed as soft watch-area **WA003** (incident-response interpretation).
- WP005 retest tomorrow (2026-05-22, CVE/vuln triage) is the natural retest home for that family of interpretation skill. If it recurs there, WA003 promotes to a WP. If it doesn't, it was one-off teaching.
- User declined revision. WP002 → MASTERED.

### Pushback as positive signal — now four consecutive sessions

| Session | Pushback target |
|---------|----------------|
| 12 | FLT Evidence A "no MD5" conclusion path; led to Evidence B sandbox-first reasoning |
| 13 | TLB file-server CIA-primary critique; tutor withdrew point (process note 15) |
| 14 | WP002 r3 format-shift goalpost; tutor agreed, process note 16 promoted; user then chose stricter accounting than tutor offered |
| 15 | WP002 remediation scope-creep on evaluation; tutor agreed, process note 17 promoted; durable feedback memory saved |

Discipline generalising outward in the right direction. Treat continued pushback as signal, not deflection.

### Hint tier log

Zero. Self-served end-to-end.

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L1 OK** | ████ 4/4 | 4 | **COMPLETE** — ready for L2; WP004 retest tomorrow |
| Bash | **L1 OK** | ████ 4/3 | 4 | **COMPLETE** — ready for L2; **WP002 MASTERED 2026-05-21** |
| Concepts | **L1 OK** | ████ 3/3 | 3 | **COMPLETE** — ready for L2; WP005 retest tomorrow |
| Scenarios | — | Locked | 0 | Unlocks when all 3 core tracks reach L2 |

---

## Active Weak Points *(WP002 closed — no longer listed here)*

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. 2026-05-15 retest clean. | 2 | 0 | **2026-05-29** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing the verification step. 2026-05-16 retest passed unprompted. | 1 | 0 | **2026-05-23** |
| WP004 | python | File iteration defaults to `f.readlines()` instead of `for line in f:`. 2026-05-15 retest passed. | 1 | 0 | **2026-05-22** |
| WP005 | concepts | Vulnerability triage skips version-check step before deciding response. 2026-05-18 first-pass missed entirely. | 0 | 0 | **2026-05-22** |

**Retest history (most recent):**
- **WP002 (2026-05-21):** ✅ **PASSED — REMEDIATION → MASTERED.** Procedural verify-don't-proxy fired unprompted; (a)/(b)/(c) order held on all three IPs; zero hint tiers. First WP closed in the programme.
- **WP002 (2026-05-19):** ❌ Failed r3 on verify-don't-proxy facet; format-shift owned by tutor; user chose strict-bar accounting. Failures 2 → 3 → triggered remediation.
- **WP003 (2026-05-16):** ✅ Passed. Fresh HMRC phishing, verification habit unprompted. Stage 0 → 1.
- **WP001 (2026-05-15):** ✅ Passed. Multi-sub-task brief, no nudges. Stage 1 → 2.
- **WP004 (2026-05-15):** ✅ Passed. Lazy iteration unprompted. Stage 0 → 1.

---

## Mastered Weak Points

| ID | Track | Mastered Date | Closed Via |
|----|-------|---------------|------------|
| WP002 | bash | 2026-05-21 | Remediation challenge ("Don't Trust the Pipeline") — both fingerprints closed (original 2026-04-28 no-count-sort + generalised 2026-05-10 trust-output-without-verification) |

---

## Watch-Areas

| ID | Track | Issue | First Observed | Promotion Trigger |
|----|-------|-------|----------------|-------------------|
| WA003 | concepts | Incident-response interpretation on credential-compromise patterns: (1) hypothetical-framing of known events, (2) slow brute-force cadence read as innocuous, (3) action-ladder with IP-block as primary on confirmed credential success, (4) priority inversion (loud-failed > quiet-succeeded). | 2026-05-21 (WP002 remediation) | One more occurrence on a Concepts L2 incident-response scenario = WP |

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable. Untouched five sessions running. Pairs naturally with Bash L2 (scripting basics).

---

## Retests Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **2026-05-22** | WP004 | Retest *(stage 1 → mastered if pass)* | python | 1 | 0 |
| **2026-05-22** | WP005 | Retest **(first)** | concepts | 0 | 0 |
| **2026-05-23** | WP003 | Retest *(stage 1 → 2 if pass)* | concepts | 1 | 0 |
| **2026-05-29** | WP001 | Retest *(stage 2 → mastered if pass)* | cross-track | 2 | 0 |

---

## Tutor Process Notes — in effect

1. One new concept per challenge at level boundaries.
2. Verify before claiming — every expected count gets the command run first.
3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
4. Brief explicitness — concrete inputs go in task descriptions, not buried in Constraints.
5. When introducing analysis frameworks, state explicitly *"if you don't know X, the lens output is verify X, not no indicator"*.
6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`.
8. Never give a working answer and ask the user to "pick" from inside it.
9. When a Tier 1 reframe gets shortcut, do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction.
10. Brief-precision miss recurs when concrete deliverables are implicit. Count concrete deliverables explicitly. **VALIDATED 2026-05-15.**
11. Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic.
12. Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1).
13. **Phishing-analysis retests test verification habit specifically when the email contains at least one lens-indicator the analyst cannot resolve from email content alone.** **VALIDATED 2026-05-16. GENERALISED 2026-05-18.**
14. *(Forming.)* When external-learning entries are noted but flagged "not sure why this matters", schedule a teach-first slot before any application slot. Origin: session 12 design-defect.
15. **Brief precision applies to the tutor as much as the user.** Every grading criterion must trace back to a property explicitly stated in the brief. **Origin 2026-05-18.**
16. **When retesting a cross-track-generalised weak point in a DIFFERENT brief format than prior retests, the new format must be telegraphed in the brief.** Otherwise the unprompted-discipline bar is unfair. **Origin 2026-05-19.**
17. **NEW 2026-05-21 — Evaluation scope must equal brief scope. If teaching territory surfaces outside the stated bar, demote it from "weakness" to "teaching observation" or schedule it for a more appropriate challenge.** **Why:** On the WP002 remediation, brief explicitly scoped to "procedural verify-don't-proxy"; user cleared that bar cleanly; review then extended marking into Concepts L2 incident-response interpretation (four points on the 203.0.113.99 analysis). User pushed back ("seriously this should be a concepts lab at this point"). Same fingerprint as process note 16 but in evaluation rather than brief design. **How to apply:** after running a review, check each flagged weakness against the brief's stated objective; if outside, surface it as teaching observation and schedule a retest in the appropriate track, do not count it against the current bar. Sibling to notes 10, 15, 16. **Saved as durable feedback memory `feedback_evaluation_scope`.**

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
- [x] **First weak point mastered — WP002** *(2026-05-21)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [x] **Portfolio has 10+ archived write-ups** *(2026-05-18 — 11 total)*

---

## Side Tasks Still Open

- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried since session 6.)*
- External courses budget decision — user has TryHackMe subscription unused.
- Redirection `<` operator: user reports never trained; introduce as new content OR amend the session-10 recall check to drop Q4.
- Vulnerable target VM install (Metasploitable2/DVWA) — highest-leverage lab unblock.

---

## Up Next

**Next session (Session 16, due 2026-05-22):** WP004 + WP005 retests. WP003 retest 2026-05-23. Then L2 content gates open with no remaining L1 gating items.
**Concepts (L2):** Available; entry pace may not need scaffolding.
**Bash (L2):** Available — scripting basics. awk-syntax revisit pairs naturally.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** Locked until all three tracks at L2.

---

## Cross-Track Connections

**7 logged.** *(Unchanged — Session 15 was retest/remediation; no new tooling-equivalence link surfaced.)*

---

## Weekly Summary

**2026-05-15 → 2026-05-21 (running):** 4 sessions (12, 13, 14, 15), ~155 minutes (~**2h 35m**) — early-week pace.
**Next formal weekly summary regenerates 2026-05-22.**

---

## Lab Status

- Ubuntu VM running (host attacker box).
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**.
- `labs/bash-L1/triage/` — reusable.
- `labs/bash-L1/retest-wp002/` — retired (r1, 2026-05-08).
- `labs/bash-L1/retest-wp002-r2/` — retired (r2, 2026-05-15).
- `labs/bash-L1/retest-wp002-r3/` — retired (r3, 2026-05-19).
- `labs/bash-L1/wp002-remediation/` — used 2026-05-21 (remediation pass). **Retain** as reference for any future cross-track-generalised remediation design.
- `python/L1/` — five scripts.
- `concepts-track/L1/` — `challenge-2-brief.md` (First Light Triage brief).
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target.

---

## Portfolio Stats

- Write-ups generated: **11** *(unchanged — Session 15 was retest/remediation)*
- Write-ups archived: **11**
- Total challenges completed: **11**
- Total challenges attempted-unfinished: 2
- Total sessions: **15** *(↑ from 14)*
- Total hours: **~13.5** *(↑ from 12.8 — Session 15 ran ~40 min wall-clock)*
- **Weak points mastered: 1** *(↑ from 0 — WP002 closed 2026-05-21)*
