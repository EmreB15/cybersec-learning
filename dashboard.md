# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-05-11 — after Session 9 (Python L1 #4 First Knock closes Python L1; write-up filled and archived in same session)*

---

## 🎯 Pickup Here

**🏆 PYTHON L1 COMPLETE 2026-05-11.** Second of three core tracks to clear L1. Closure conditional on WP004 retest 2026-05-14.

**Next session: 5 retests / recall checks on schedule before new L2 content.**

> 📌 **Retest queue (priority order):**
> 1. **WP002 — due 2026-05-12** *(bash frequency-count discipline; failures = 1, stage 0; **third failure triggers a remediation challenge** — highest-stakes retest. WP002's generalised description now has THREE cross-language data points: bash sort-column round 1 → python predicate-proxy session 8 → python exception-class session 9. Pattern is durable: trust the one observation without probing the class.)*
> 2. **WP003 — due 2026-05-14** *(concepts phishing analysis; verification-habit on a NEW phishing email — fresh email needed, prepare in advance)*
> 3. **WP004 — due 2026-05-14** *(python file iteration; needs a challenge that exposes a real or simulated large-file scenario so the readlines footgun is visible. **Two positive signals holding** — Brute Force Source used lazy iteration unprompted; First Knock used `try/except` cleanly with no readlines-style memory misstep.)*
> 4. **Redirection recall check — due 2026-05-14** *(forward-looking recall check at user's proactive request, NOT a WP. 4 cold prompts on operator behaviour, no scaffold, no scrollback.)*
> 5. **WP001 — due 2026-05-15** *(cross-track instruction precision; stage 1 → 2 if pass. **Evidence mixed:** session 8 soft failure (Password Auditor brief-precision miss); session 9 CLEAN PASS (First Knock brief enumerated two test cases; both exercised without nudge — third L1 in a row clean on enumeration discipline). Design retest as multi-sub-task brief to test execution discipline directly.)*

> 🗺️ **After retests — user picks new content from:**
> - **Bash L2 #1** — first Bash L2 challenge. Scripting basics (variables, loops, conditionals, exit codes). Lab depends on choice: file organiser/log monitor reuse existing labs; ping sweep needs Metasploitable target.
> - **🆕 Python L2 #1** — NEW. First Python L2 challenge. Tool-building (subprocess, argparse, pipe-friendly output). Examples: **port scanner** (scales today's First Knock primitive across a port range with concurrency), subdomain enumerator, log anomaly detector, hash identifier.
> - **Concepts L1 #2** — likely network/CIA reasoning scenario; **still deferred until WP003 retest passes 2026-05-14.**

> 🔧 **Tutor process — confirmed in effect:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
> 7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`. Use *"two paths together"* or list with commas.
> 8. Never give a working answer and ask the user to "pick" from inside it. Either give the answer cleanly OR show a placeholder for them to fill — not both.
> 9. When a Tier 1 reframe gets shortcut (user takes the easier step and stops), do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction. *(Validated session 8 — Password Auditor.)*
> 10. Brief-precision miss recurs when concrete deliverables are implicit. When designing briefs, count concrete deliverables explicitly (e.g. "two test cases — both must be exercised"); don't bury the "all of them" requirement in narrative.
> 11. **NEW (2026-05-11):** Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic. *(Validated session 9 — First Knock: 3 reframes no escalation, full unblock.)*
> 12. **NEW (2026-05-11):** Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1; target must be own machine / own VM / written-authorisation lab). Restate in shorter form at start of each subsequent network challenge.

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried forward from session 6.)*
- External courses budget decision — user has TryHackMe subscription unused. Session 8 recommendations stand: TryHackMe Cyber Security 101 path → Jr Pen Tester / SOC Analyst L1; PortSwigger Web Security Academy (free, defer to Python L2 — **Python L2 now unlocked**); OverTheWire Bandit (free, alongside Bash L2). Recommend tagging one THM room per week as *"session homework"*.

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — with Python L2 now unlocked alongside Bash L2, this is the highest-leverage side task to unblock the broadest L2/L3 paths.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | **L1 ✅** | ████ 4/4 | 4 | **✅ COMPLETE 2026-05-11** — second track to clear L1; ready for L2 |
| 🖥️ Bash | **L1 ✅** | ████ 4/3 | 4 | **✅ COMPLETE 2026-05-10** — first track to clear L1; ready for L2 |
| 🔐 Concepts | L1 | █░░ 1/3 | 1 | 🟡 Active but deferred — WP003 retest gates next challenge |
| 🎭 Scenarios | — | Locked | 0 | 🔒 Unlocks when all 3 core tracks reach L2 |

**Two L1 closures in 24h.** With Python L1 + Bash L1 both clear, the path to scenario unlock is: Bash L2 + Python L2 + Concepts L2.

---

## 📝 Session 9 Summary (2026-05-11 — 1h15-locked session)

### ✅ Python L1 #4 — First Knock (`port_check.py`) — CLOSES PYTHON L1

- **New concept zone:** TCP connection attempt as port-state probe. First Python challenge to touch the `socket` module. Function signature: `check_port(host, port, timeout=1.0)` → `True`/`False`. Logic: `socket.create_connection((host, port), timeout)` inside `try/except OSError`. Success path returns True; any caught socket-level failure returns False. Two test calls on 127.0.0.1 (port 8080 with `http.server` listener → OPEN; port 9999 → CLOSED).
- **Concepts that landed:** `socket.create_connection` as a probe primitive; exception-as-failure-signal control flow (success returns, failure raises); `OSError` as parent class of all socket connection failures per PEP 3151 (`ConnectionRefusedError`, `TimeoutError`, `ConnectionResetError`, `socket.gaierror`); resource cleanup via explicit `.close()` on the success path; bounded wait via `timeout` argument.
- **🎯 Sustained Tier 1 carried the full unblock — no tier escalation:**
  1. *"When 9999 is closed, what does create_connection actually do on that line?"* — user answered "returns a socket."
  2. *"Test it — add `print(socket_1)`, run against 9999, observe."* — user ran, reported `TimeoutError`.
  3. *"How do you write code that runs one way when a line succeeds, and a different way when that line raises?"* — user reached for `try/except` and wrote a clean structure.
  - Pattern: when the gap is conceptual not syntactic, Tier 1 can carry an entire challenge if reframes are well-staged. Different shape from session 8's shortcut pattern.
- **🟡 Moderate weakness (caught in review, fixed in same revision):** revision 1 caught only `TimeoutError`. Brief had explicitly named three failure modes (refused, timeout, otherwise fails) — fix on revision 2: `except OSError`. Same WP002 family fingerprint as session 8's predicate-proxy bug — empirically observe one failure mode, generalise to the whole class without probing the rest. **THIRD CROSS-LANGUAGE INSTANCE in three sessions** (bash sort-column → python predicate-proxy → python exception-class). Not opening new WP; WP002's generalised description already covers it.
- **🟢 Minor cleanups (same revision):** stripped `source_address=None` default-arg noise; added explicit `socket.close()` on success path (foundation for L2's multi-port scanner where the leak would matter).
- **WP001 POSITIVE SIGNAL:** brief enumerated two test cases; both exercised without nudge. Third L1 challenge in a row clean on enumeration discipline (Brute Force Source clean, Password Auditor needed nudge, First Knock clean).
- **⚖️ Ethics framing delivered pre-challenge:** first network-touching Python challenge. UK Computer Misuse Act 1990 §1 named; rule stated for the programme — target must be (a) own machine, (b) own VM, (c) written-authorisation lab. Today restricted to `127.0.0.1` only. ⚠️ Verify markers on case-law citations (DPP v Bignell, R v Bow Street Magistrates ex parte US No 2) — surfaced from memory, primary-source verification not run in session.

### 📝 Write-up filled and archived in same session

Cleanup pass: 3 user-fillable sections completed; 8 copyedits applied (capital I ×5, comma splice, present-tense, backticks on `TimeoutError`/`OSError`, typo `excpet` → `except`, past-tense agreement). Voice preserved on technical claims (kept "port scanner" phrasing and "closed socket" phrasing).

### 🔧 Tutor process notes carried forward

- **Sustained Tier 1 validated** — three reframes same mode, no escalation, full unblock. Different shape from session 8's shortcut pattern. Both are tools; the right one depends on the gap shape.
- **Brief-precision discipline now has three L1 data points** — 2 clean (Brute Force Source, First Knock), 1 nudge (Password Auditor). Trajectory is positive; 2026-05-15 WP001 retest will read the trend.

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. **Mixed session 8/9 evidence:** session 8 soft failure (Password Auditor); session 9 **CLEAN PASS** (First Knock brief enumerated two test cases, both exercised without nudge). | 1 | 0 | **2026-05-15** |
| WP002 | bash | Frequency-count pipelines: skips count-column sorting, trusts pipeline output without inspecting intermediate stages. **Generalisation 2026-05-10:** broader pattern is *trust visible output without inspecting adjacent evidence that contradicts the assumption*. **THREE CROSS-LANGUAGE DATA POINTS now**: bash sort-column round 1 (2026-04-28), python predicate-proxy (2026-05-11 s8), python exception-class (2026-05-11 s9). Same fingerprint each time — empirically observe one path, generalise to whole class. Pattern is durable. | 0 | **1** | **2026-05-12** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step the lens requires (method gap, not knowledge gap) | 0 | 0 | **2026-05-14** |
| WP004 | python | File iteration defaults to `f.readlines()` (eager, full-file load) instead of iterating the file object directly (lazy). Crashes on production-scale logs. **Two positive signals holding:** Brute Force Source unprompted lazy iteration; First Knock used `try/except` cleanly with no readlines-style memory misstep. Prognosis good but still test on a NEW twist with large-file scenario. | 0 | 0 | **2026-05-14** |

**Cross-track pattern note:** WP002 (bash, skip-the-inspection-step), WP003 (concepts, skip-the-verification-step), and the session 8/9 python instances (use-a-cheap-proxy-instead-of-the-real-test; generalise-from-one-observation) may all be the same underlying habit — *infer the answer without doing the named verification step*. **Three retests in the next 5 days plus the new session-9 data point will give us a clear read.**

**Retest history:**
- **WP001 (2026-05-08):** ✅ Passed. Brief Precision: 3 sub-tasks, all parameters exactly as briefed, single-tool answers.
- **WP002 (2026-05-08):** ❌ Failed. Frequency Recall: correct answer surfaced but missed `Failed`-only filter and intermediate inspection (both explicit brief criteria).

> ℹ️ **WP002 description history:** earlier evidence of *"`sort -r` would misrank counts ≥10"* was empirically falsified 2026-05-08. The round-1 bug from Trail in the Logs (no count-column sort at all) remains real. The 2026-05-10 generalisation broadened the description beyond frequency-counting; the 2026-05-11 cross-language pattern observations (session 8 + session 9) strengthen it to three independent data points across two languages.

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
| **2026-05-14** | Redirection refresher | Recall check (not WP) | bash | — | — |
| **2026-05-15** | WP001 | Retest | cross-track | 1 → 2 if pass | 0 |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour)*
- [x] **All three core tracks active at L1** *(2026-05-10)*
- [x] **First track reaches Level 1 complete — Bash L1 ✅** *(2026-05-10 — Evidence Trail closed redirection criterion)*
- [x] **Second track reaches Level 1 complete — Python L1 ✅** *(2026-05-11 — First Knock closed the level)*
- [ ] All tracks reach Level 1 complete *(Concepts 1/3 remaining)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups *(currently 9 — 1 to go)*

---

## 🗺️ Up Next

**Bash (L2):** First L2 challenge available — scripting basics (variables, loops, conditionals, exit codes). CLAUDE.md L2 examples: ping sweep (lab-only — gated on Metasploitable install), log monitor, file organiser. Lab choice unblocks specific challenges.
**Python (L2):** 🆕 First L2 challenge unlocked. Tool-building (subprocess, argparse, pipe-friendly output). Examples: port scanner (scales First Knock primitive across a range with concurrency), subdomain enumerator, log anomaly detector, hash identifier.
**Concepts (L1):** Challenge #2 — network or CIA-triad reasoning. **Still deferred** until WP003 retest passes 2026-05-14.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**7 logged.** *(+1 from session 9: Python `socket.create_connection` ↔ Bash `nc -zv` / `</dev/tcp/host/port` — single-port TCP probe primitive, shared legality gate.)*

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]`. Bash version is pipe-ready one-shot; Python version composes inside larger scripts.
- *2026-04-28* — **Bash ↔ Python**: frequency analysis. Bash: `... | sort | uniq -c | sort -nr | head`. Python: `Counter(iterable).most_common(N)`. Same gotcha in both: default sort/min/max on numeric strings is lexicographic.
- *2026-04-28* — **Bash ↔ Python**: positional field extraction is fragile. `awk '{print $11}'` and `line.split()[10]` both break when log format shifts. Real fix: regex on value *shape*.
- *2026-05-10* — **Bash ↔ Python**: log line filtering by substring. Bash: `grep "Failed" auth.log`. Python: `with open(path) as f: for line in f: if "Failed" in line: print(line, end="")`. **Asymmetric gotcha:** Python defaults to a `f.readlines()` footgun that Bash `grep` doesn't have because it streams.
- *2026-05-10* — **Bash ↔ Python**: positional field extraction via `.split()[N]` mirrors `awk '{print $N}'`. Python's `.split()` with no args matches awk's default whitespace handling — both reward token-based parsing over byte-based parsing. **Brittleness identical**: index points at wrong field if log format shifts.
- *2026-05-10* — **Python → Bash**: script output captured to file via Bash redirection (`>`). Real triage workflow — Python script extracts/parses; Bash redirection captures output for handoff. Same `>` vs `>>` decision as Evidence Trail Tasks 1 and 2: overwrite for snapshot data, append for accumulation.
- *2026-05-11* — **Python ↔ Bash**: single-port TCP availability check. Python: `socket.create_connection((host, port), timeout)` inside `try/except OSError`. Bash: `nc -zv host port` (netcat zero-IO probe, exit 0 = open) or `timeout 1 bash -c "</dev/tcp/host/port"` (bash built-in pseudo-device). Python wins for composable tooling (output capture, loops, parallel scanning); Bash wins as one-shot pipe-ready probe. **Shared legality gate** — probes against hosts you don't own = unauthorised access under UK CMA 1990 §1.

---

## 📈 Weekly Summary

**2026-05-05 → 2026-05-11 (rolling 7-day):** 5 sessions, ~430 minutes total (~**7h 10m**). Comfortably above 5h target, well below 12h drift threshold. Strong week — seven challenges completed in this rolling window: Bash L1 Find Tour, Concepts L1 #1, Python L1 #1, Bash L1 Evidence Trail (closes Bash L1), Python L1 #2, Python L1 #3, **Python L1 #4 (closes Python L1)**. Two L1 closures inside 24 hours. Next formal weekly summary regenerates 2026-05-15.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box).
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**. With both Python L2 and Bash L2 now unlocked, this is the highest-leverage side task. Required before any scanning / network challenge against a non-local target. Gates Bash L2 ping sweep and most Python L3 work.
- ✅ `labs/bash-L1/triage/` — reusable; lab contents from Evidence Trail still in place.
- ✅ `labs/bash-L1/retest-wp002/auth-snippet.log` — reusable for 2026-05-12 WP002 retest.
- ✅ `python/L1/` — now contains four scripts: `log_filter.py`, `ip_extractor.py`, `password_audit.py`, `port_check.py`. Python L1 directory complete.
- ℹ️ **Localhost as a lab target:** First Knock established `127.0.0.1` as a fully-legal test target for Python socket work (your own machine, no CMA concern). Pattern available for any L1/early-L2 work that needs a listening service without a separate target VM (`python3 -m http.server <port>` for HTTP-ish, `nc -l <port>` for raw TCP).

---

## 📁 Portfolio Stats

- Write-ups generated: **9** *(↑ from 8 — First Knock archived 2026-05-11)*
- Write-ups archived (with reflections filled): **9** *(↑ from 8 — full archive parity, all 9 generated write-ups archived)*
- Total challenges completed: **9** *(↑ from 8)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **9** *(↑ from 8)*
- Total hours: **~9.4** *(↑ from 8.4)*
