# Cybersecurity Training Dashboard
*Last updated: 2026-05-18 — after Session 13 (Concepts L1 #3 Three Loose Bricks complete; CLOSES CONCEPTS L1; ALL THREE CORE TRACKS NOW AT L1 COMPLETE; write-up template generated, archive pending user fill)*

---

## Pickup Here

**SESSION 14 NEXT — WP002 retest is TOMORROW (2026-05-19) and remains the single highest-stakes item on the board.** Failures = 2; one more failure triggers a remediation challenge. Design as a fresh bash frequency-count with the **retest-wp002-r3** dataset (generate before session). The verify-don't-proxy discipline must fire **unprompted** on first submission.

**Session 13 closed 2026-05-18** — second 30-min session of the same calendar day. Concepts L1 #3 'Three Loose Bricks' complete, attack-surface analysis on small-org flat-/24 network. Write-up template at [writeups/concepts-L1-three-loose-bricks-2026-05-18.md](writeups/concepts-L1-three-loose-bricks-2026-05-18.md) — **awaiting user fill**, then autonomous wrap-publish flow fires (cleanup → archive → stage → commit → push, single motion).

🏆 **CHECKPOINT HIT: ALL THREE CORE TRACKS AT L1 COMPLETE.** Bash 2026-05-10, Python 2026-05-11, Concepts 2026-05-18. 13 sessions over 21 calendar days. From zero-domain-knowledge diagnostic 2026-04-27 to all-tracks-L1 in three weeks.

> **Retest queue (priority order):**
> 1. **WP002 — due 2026-05-19 TOMORROW** *(bash frequency-count discipline; failures = 2, stage 0; **next failure = remediation challenge** — highest-stakes retest on the board)*
> 2. **WP004 — due 2026-05-22** *(python file iteration; stage 1; one more clean retest = mastered)*
> 3. **WP005 — due 2026-05-22** *(concepts vuln triage / version-check before action; stage 0; first retest checks if NVD-first habit fires unprompted)*
> 4. **WP003 — due 2026-05-23** *(concepts phishing analysis; stage 1; one more clean retest = stage 2)*
> 5. **WP001 — due 2026-05-29** *(cross-track instruction precision; stage 2; one more clean retest = mastered)*

> **New content options (sessions beyond the WP002 retest) — NOW INCLUDES CONCEPTS L2:**
> - **Bash L2 #1** — scripting basics (variables, loops, conditionals, exit codes). File organiser / log monitor reuse existing labs; ping sweep needs Metasploitable.
> - **Python L2 #1** — tool-building (subprocess, argparse, pipe-friendly output). Port scanner scales First Knock primitive across a range with concurrency.
> - **Concepts L2 #1 (NEW — just unlocked)** — vulnerability classes / attack methodologies / defence frameworks. Map to TM256 chapters where applicable. **Entry pace may not need scaffolding** given the L2-shape reasoning showing reliably at L1 in the last three Concepts challenges (FLT Evidence B sandbox-then-submit, TLB original Reception→file-server chain, TLB revision CCTV→social-engineering chain).

> **Spaced-repetition flag (carried forward, untouched three sessions running now):**
> - **awk action-block syntax** — third L0/L1 exposure on session 10 still needed full T1→T2→T3 escalation; user reports "awk just doesn't sit in my mind". Treat as syntax-recall gap, not conceptual. Schedule a short revisit alongside next bash work (fits naturally with the WP002 retest tomorrow).

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
> 13. **Phishing-analysis retests test verification habit specifically when the email contains at least one lens-indicator the analyst cannot resolve from email content alone.** **VALIDATED 2026-05-16.** **GENERALISED 2026-05-18** — same principle applied to Evidence C of First Light Triage; trap fired, gap surfaced, WP005 logged.
> 14. **(Forming, not yet formal.)** When external-learning entries are noted but flagged "not sure why this matters", do NOT assume the next challenge can run without re-teaching — schedule a teach-first slot before the application slot. Origin: session 12 design-defect.
> 15. **NEW 2026-05-18 — Brief precision applies to the tutor as much as the user.** If an evaluation depends on a property X, X must be stated in the brief, not inferred from domain knowledge the user doesn't yet have. **Origin:** 2026-05-18 'Three Loose Bricks' — tutor flagged file server CIA primary as Confidentiality because in real Windows/SMB Modify permission includes Read by default. Brief had only stated 'writable by everyone in Domain Users'. User pushed back; point withdrawn. **How to apply:** when writing review criticisms, every grading criterion must trace back to a property explicitly stated in the brief. Sibling to note 10 (count concrete deliverables explicitly) and note 13 (verify-or-skip trap design — explicit signals in the brief).

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
| Concepts | **L1 OK** | ████ 3/3 | 3 | **COMPLETE 2026-05-18** — ready for L2; entry pace may not need scaffolding |
| Scenarios | — | Locked | 0 | Unlocks when all 3 core tracks reach L2 |

---

## Session 13 Summary (2026-05-18 — 30-min planned, ~35-min actual including pause/resume)

### Challenge run

**Concepts L1 #3 Three Loose Bricks** — attack-surface analysis on a small-org flat-/24 network description (ACME Marketing). Pattern selected to differ from prior two L1 challenges (no phishing, no threat-intel triage). 5 described items: reception desktop, file server (Win Server 2016), Wi-Fi (WPA2-PSK shared with guests on card), CCTV recorder (default admin/admin), bookkeeper laptop (cleartext FTP).

### Session shape

Started 10:25. ~15 min into the 30-min slot user submitted three top-3 picks. Tutor delivered review flagging the CCTV miss as 🔴 Critical. **User pushed back on the file server CIA-primary critique** — tutor brief had only stated "writable", so grading on Confidentiality (which requires Read-also access in real Windows/SMB) was inferring from domain knowledge not in the brief. Point withdrawn. User then ran out of time mid-revision and explicitly requested *"keep this conversation here i will be back to finish it"* — **pause, not lock**. Returned same day, submitted revised top-3 (CCTV slotted in at #2 per option (b), Reception swapped out). Tutor reviewed revision, confirmed L1 closure, ran wrap-publish flow.

### First-submission top-3

1. **Wi-Fi (Confidentiality):** Led with operational fact (passphrase printed on card given to guests), not theoretical WPA2-PSK weakness. ✅ Correct top pick.
2. **Reception desktop (Integrity):** Reasoning was about attribution (no audit trail). 🟡 Underweighted the trivially-guessable password `Reception2023`. **Strong:** pivot/lateral-movement reasoning explicit — "get access to this desktop carry out an attack to the file server, then leave" — L2 shape at L1.
3. **File server (Integrity):** Over-broad write access in Domain Users. ✅ Defensible top-3 candidate.

**Critical miss (🔴):** CCTV recorder (item 4 of brief — default `admin/admin` verbatim, on flat network) **unranked entirely**. Plausibly top-2 by effort-to-impact ratio. Zero-skill exploit; high-impact pivot (embedded Linux box on flat network = attacker foothold + intelligence-gathering sensor). Real-world: most breaches start at the unloved IoT/default-cred device, not the well-tended file server.

### Tutor error owned in session

Original review flagged file server CIA primary as Confidentiality on grounds that real Windows/SMB Modify permission includes Read by default. Brief had only stated *"writable by everyone in the Domain Users group"*. User pushed back. **Point withdrawn cleanly.** Process note 15 promoted: brief precision applies to the tutor as much as the user — if an evaluation depends on a property X, X must be stated in the brief, not inferred from domain knowledge the user doesn't yet have.

### Revised top-3 (option (b) — Reception swapped out for CCTV)

1. **Wi-Fi (Confidentiality)** — unchanged.
2. **CCTV recorder (Confidentiality)** — chained the foothold to next-stage technique. **User went past tutor prompt** — added physical-surveillance angle (cameras watching screens, faces, swipe cards = social-engineering preparation) that tutor had not named. Intelligence-gathering reasoning on top of network reasoning. Minor nits (not WPs): "easy to guess" framing on credentials (sharper: "default credentials shipped with device" — CIS Control 4); "spy on network transmissions" implies passive sniffing on a switched LAN (mechanism slightly off — modern switched networks require ARP spoofing / MITM).
3. **File server (Integrity)** — unchanged from original.

### Hint tier log

**Tier 0** across both original submission and revision. Solo throughout.

### Honesty discipline — pushback as positive signal

User pushback on tutor evaluation is itself the WP003 verify-don't-proxy discipline applied to tutor review, not just to scenario evidence. The discipline is generalising outward — from "don't substitute confidence on phishing lenses" → "don't substitute confidence on tutor critique." Recorded as positive signal; should not be softened by treating future pushback as deflection.

### Pivot reasoning — now consistent across three consecutive Concepts L1 challenges

| Challenge | Pivot evidence |
|-----------|----------------|
| FLT Evidence B | "Sandbox first, then submit to VT" — SOC analyst pattern, L2/L3 territory at an L1 task |
| TLB original | Reception desktop → file server chain — lateral-movement thinking explicit |
| TLB revision | CCTV foothold → social-engineering preparation chain — multi-stage reasoning |

L2 shape showing reliably at L1. Informs Concepts L2 entry calibration — scaffolded entry may not be required.

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. 2026-05-15 retest clean pass on explicitly-enumerated brief. | 2 | 0 | **2026-05-29** |
| WP002 | bash | Frequency-count pipelines / verify-don't-proxy generalisation: trust visible output without inspecting adjacent evidence. 2026-05-15 retest FAILED. | 0 | **2** | **2026-05-19 ⚠️** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step. 2026-05-16 retest PASSED unprompted on trap lenses. | 1 | 0 | **2026-05-23** |
| WP004 | python | File iteration defaults to `f.readlines()` instead of `for line in f:`. 2026-05-15 retest PASSED. | 1 | 0 | **2026-05-22** |
| WP005 | concepts | Vulnerability triage skips version-check step before deciding response. 2026-05-18 first-pass missed entirely; revision passed concept but kept wrong tool (exploit-db, not NVD). | 0 | 0 | **2026-05-22** |

**Cross-track pattern note — UNCHANGED 2026-05-18.** WP002 (bash frequency-count), WP003 (concepts phishing analysis), and WP005 (concepts vuln triage) remain three concrete instances of the same underlying habit — *skip the named verification step* — in three different domains. WP002 retest tomorrow remains the highest-stakes test of whether the habit is generalising in the right direction. TLB challenge did not test the verify-or-skip trap cleanly because the items requiring verification (cleartext FTP, Windows Server 2016 patch state) did not make the user's top 3 — discipline was not exercised in this challenge.

**Retest history (most recent):**
- **WP003 (2026-05-16):** ✅ PASSED. Fresh HMRC phishing, verification habit unprompted. Stage 0 → 1.
- **WP001 (2026-05-15):** ✅ PASSED. Multi-sub-task brief, no nudges. Stage 1 → 2.
- **WP002 (2026-05-15):** ❌ FAILED. Same fingerprint as 2026-05-08. Failures 1 → 2.
- **WP004 (2026-05-15):** ✅ PASSED. Lazy iteration unprompted. Stage 0 → 1.

---

## Watch-Areas

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable. Untouched sessions 11, 12, 13. Fits naturally with the WP002 retest tomorrow.

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
- [x] **🏆 ALL TRACKS REACH LEVEL 1 COMPLETE** *(2026-05-18 — Concepts L1 closed by Three Loose Bricks)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [x] **Portfolio has 10+ archived write-ups** *(2026-05-18 — First Light Triage archived; 10 total)*

---

## Up Next

**Tomorrow (2026-05-19):** WP002 retest — single highest-stakes item on the board.
**Concepts (L2 — newly unlocked):** Available; entry pace may not need scaffolding (L2 reasoning shape showing reliably at L1 in last three challenges).
**Bash (L2):** Available — scripting basics. Awk-syntax revisit fits here too.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** Locked until all three tracks at L2.

---

## Cross-Track Connections

**7 logged.** *(Unchanged — Session 13 was reasoning-based, no new tooling-equivalence link surfaced.)*

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

- Write-ups generated: **11** *(↑ from 10 — Three Loose Bricks template)*
- Write-ups archived: **10** *(unchanged — Three Loose Bricks awaiting user fill)*
- Total challenges completed: **11** *(↑ from 10)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **13** *(↑ from 12)*
- Total hours: **~12.0** *(↑ from 11.5)*
