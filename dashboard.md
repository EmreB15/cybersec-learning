# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-05-11 — after Session 8 (Password Auditor closes Python L1 #3; write-up generated, awaiting fill; external-courses meta question addressed pre-session)*

---

## 🎯 Pickup Here

**Next session: 5 retests/recall checks still on schedule before/interleaved with new content.**

> 📌 **Retest queue (priority order — unchanged from session 7 plan):**
> 1. **WP002 — due 2026-05-12** *(bash frequency-count discipline; failures = 1, stage 0; **third failure triggers a remediation challenge** — highest-stakes retest. Cross-track signal from session 7 broadened the WP description; session 8 added a one-shot self-correction in the same family — predicate-proxy bug `c.upper() == c` — same verification-vs-proxy lesson, different language, not WP-promoted because single occurrence.)*
> 2. **WP003 — due 2026-05-14** *(concepts phishing analysis; verification-habit on a NEW phishing email — fresh email needed, prepare in advance)*
> 3. **WP004 — due 2026-05-14** *(python file iteration; needs a challenge that exposes a real or simulated large-file scenario so the readlines footgun is visible. **Positive signal from Brute Force Source still holding** — prognosis good but still test on a NEW twist.)*
> 4. **Redirection recall check — due 2026-05-14** *(forward-looking recall check at user's proactive request, NOT a WP. 4 cold prompts on operator behaviour, no scaffold, no scrollback.)*
> 5. **WP001 — due 2026-05-15** *(cross-track instruction precision; stage 1 → 2 if pass. **NEW soft evidence from session 8** — brief-precision miss recurred on Password Auditor; design the retest as a multi-sub-task brief to test brief-execution discipline directly.)*

> 🗺️ **After retests — user picks new content from:**
> - **Bash L2 #1** — first L2 challenge. Scripting basics (variables, loops, conditionals, exit codes). Lab depends on choice: file organiser/log monitor reuse existing labs; ping sweep needs Metasploitable target.
> - **🆕 Python L1 #4** — closes Python L1. Likely socket basics, IP validator, or another L1-grade concept (avoid repeating password / auth-log territory).
> - **Concepts L1 #2** — likely network/CIA reasoning scenario; **still deferred until WP003 retest passes**.

> 🔧 **Tutor process — confirmed in effect:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
> 7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`. Use *"two paths together"* or list with commas.
> 8. Never give a working answer and ask the user to "pick" from inside it. Either give the answer cleanly OR show a placeholder for them to fill — not both.
> 9. **NEW (2026-05-11):** When a Tier 1 reframe gets shortcut (user takes the easier step and stops), do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction. *(From Password Auditor "without hardcoding" — worked: abstraction landed on revision 2.)*
> 10. **NEW (2026-05-11):** Brief-precision miss recurs when concrete deliverables are implicit. When designing briefs, count concrete deliverables explicitly (e.g. "four test passwords — all four must be exercised"); don't bury the "all of them" requirement in narrative.

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried forward from session 6.)*
- **🆕 External courses budget decision** — user has TryHackMe subscription unused. Session 8 recommendations: TryHackMe Cyber Security 101 path → Jr Pen Tester / SOC Analyst L1; PortSwigger Web Security Academy (free, defer to Python L2); OverTheWire Bandit (free, alongside Bash L2). Recommend tagging one THM room per week as *"session homework"* so the tutor can convert external exposure into portfolio.

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — gates Bash L2 ping sweep, most Python L3 work. Consider as a side task if user wants to unblock the broadest L2/L3 paths.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | L1 | ███░ 3/4 | 3 | 🟢 Active — third clean challenge; one remaining to close L1 |
| 🖥️ Bash | **L1 ✅** | ████ 4/3 | 4 | **✅ COMPLETE 2026-05-10** — first track to clear L1; ready for L2 |
| 🔐 Concepts | L1 | █░░ 1/3 | 1 | 🟡 Active but deferred — WP003 retest gates next challenge |
| 🎭 Scenarios | — | Locked | 0 | 🔒 Unlocks when all 3 core tracks reach L2 |

**Python L1 close-out:** one more L1 challenge to clear the level. Recommend avoiding password / auth-log territory next — three of the four L1 challenges have been in that space; final one should diversify (socket basics, IP validator, password strength variant in a different domain, or similar).

---

## 📝 Session 8 Summary (2026-05-11 — 60-min focused session)

### ✅ Python L1 #3 — Password Auditor (`password_audit.py`)

- **One new concept zone:** input validation — first Python L1 challenge outside log-parsing. `audit(password)` evaluates against four criteria (length ≥ 12, ≥ 1 uppercase, ≥ 1 lowercase, ≥ 1 digit) and returns `(verdict_bool, failed_labels_list)`; caller loops four test passwords and formats output per case.
- **Concepts that landed:** string predicate methods (`.isupper()` / `.islower()` / `.isdigit()`), boolean composition with `and` chain, **list-as-accumulator pattern** for dynamic output, tuple return + tuple unpacking, `", ".join()` for delimited list-to-string.
- **🌟 Convergent-fix moment on revision 2:** the list+join refactor simultaneously closed three issues — the *"without hardcoding"* output question, the brief's required return type (tuple of bool + list), and the trailing-comma bug in earlier string-concat output. **One refactor closed three problems.** That kind of convergence is the lesson; remember it as a teaching moment.
- **🔴 Critical bug self-corrected:** first version used `c.upper() == c` and `c.lower() == c` as proxies for is-uppercase / is-lowercase. The proxy is True for any character without case (digits, spaces, punctuation) — so a password like `"abcdef12345678"` would falsely satisfy a "must contain uppercase" check. Bug was hidden by the four test passwords. Concept nudge in review 1 ("what's another built-in like `.isdigit()`?"); self-corrected to `.isupper()` / `.islower()` on first revision. **Single occurrence, lesson landed — not opening a new WP.** **Same family as WP002's broader generalisation** — verify what you claim, not a proxy that doesn't hold under adversarial input. Language-independent lesson.
- **🟡 Brief-precision miss (WP001 family):** first two submissions called `audit()` on only one of four required test passwords. Closed on revision 3 after explicit nudge. **Soft WP001 evidence logged** — not a formal retest failure, but the pattern recurred.
- **Positive signals:**
  - **Boundary-case precision (proactive):** user asked at challenge start whether length 12 satisfies *"at least 12"* — verify-before-coding instinct on an off-by-one bug class.
  - **Micro-optimisation discipline (engineering discussion):** user defended `and not one_X` per-predicate guards on efficiency grounds. Discussion separated outer break (real win on long happy-path inputs, kept) from inner guards (micro-opt at password-sized inputs, dropped on consistency grounds — three predicate checks now read symmetrically). User dropped the guards correctly. Principle stated: optimise for readability first; reach for micro-opts only when profile data tells you to.

### 💬 External courses meta-question — addressed pre-session

User asked which external courses complement the tutor work. Read of the landscape:

- **Tier 1 (use these soon):**
  - **TryHackMe (subscription already paid for):** Cyber Security 101 path now; Jr Pen Tester or SOC Analyst L1 once Python/Bash are deeper. London market signal.
  - **PortSwigger Web Security Academy (free):** industry standard for web app security; defer to Python L2.
  - **OverTheWire Bandit (free):** Bash/Linux wargame; run alongside Bash L2.
- **Tier 2 (later):** Security+ (UK recruiter cert, defer 9-12 months); HackTheBox Academy CPTS (later); LetsDefend (blue-team option).
- **Skip:** Udemy mega-bundles, premature OSCP.
- **Recommended cadence:** tag one TryHackMe room per week as *"session homework"*; bring scripts/questions back here so external exposure converts into portfolio.

### 🔧 Tutor process notes carried forward

- **Tier 1 reframe shortcut pattern confirmed:** when user takes the easier step inside a Tier 1 reframe and stops, don't escalate tiers during the challenge — flag in review, let revision force the abstraction. Worked on the *"without hardcoding"* question.
- **Brief-precision miss recurred** (call-on-4 vs call-on-1). Designing the 2026-05-15 WP001 retest as an explicit multi-sub-task brief will test the pattern directly.

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. **New soft evidence 2026-05-11** — Password Auditor brief miss (call on 1 of 4 test passwords; needed nudge to close on revision 3). | 1 | 0 | **2026-05-15** |
| WP002 | bash | Frequency-count pipelines: skips count-column sorting, trusts pipeline output without inspecting intermediate stages. **Generalisation 2026-05-10:** broader pattern is *trust visible output without inspecting adjacent evidence that contradicts the assumption*. **Session 8 cross-pattern note:** Python predicate-proxy bug (`c.upper() == c`) is the exact same shape in different language — verify what you claim, not a proxy. Self-corrected; not WP-promoted but worth noting the pattern is durable across language. | 0 | **1** | **2026-05-12** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step the lens requires (method gap, not knowledge gap) | 0 | 0 | **2026-05-14** |
| WP004 | python | File iteration defaults to `f.readlines()` (eager, full-file load) instead of iterating the file object directly (lazy). Crashes on production-scale logs. **Positive signal 2026-05-10:** lazy iteration used unprompted in Brute Force Source — prognosis good but still test on new twist. | 0 | 0 | **2026-05-14** |

**Cross-track pattern note:** WP002 (bash, skip-the-inspection-step), WP003 (concepts, skip-the-verification-step), and the session 8 predicate-proxy bug (python, use-a-cheap-proxy-instead-of-the-real-test) may all be the same underlying habit — *infer the answer without doing the named verification step*. **Three retests in the next 5 days plus the new session-8 self-correction data point will give us a clear read.**

**Retest history:**
- **WP001 (2026-05-08):** ✅ Passed. Brief Precision: 3 sub-tasks, all parameters exactly as briefed, single-tool answers.
- **WP002 (2026-05-08):** ❌ Failed. Frequency Recall: correct answer surfaced but missed `Failed`-only filter and intermediate inspection (both explicit brief criteria).

> ℹ️ **WP002 description history:** earlier evidence of *"`sort -r` would misrank counts ≥10"* was empirically falsified 2026-05-08. The round-1 bug from Trail in the Logs (no count-column sort at all) remains real. The 2026-05-10 generalisation broadens the description beyond frequency-counting; the 2026-05-11 cross-language pattern observation strengthens it further.

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
- [ ] All tracks reach Level 1 complete *(Python 3/4, Concepts 1/3 remaining)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups *(currently 7 — 3 to go; today's write-up pending fill)*

---

## 🗺️ Up Next

**Bash (L2):** First L2 challenge available — scripting basics (variables, loops, conditionals, exit codes). CLAUDE.md L2 examples: ping sweep (lab-only — gated on Metasploitable install), log monitor, file organiser. Lab choice unblocks specific challenges.
**Python (L1):** 🆕 Challenge #4 — closes the level. Likely socket basics, IP validator, or a different L1-grade concept (avoid repeating password / auth-log territory — three of four L1 challenges have lived in that space).
**Concepts (L1):** Challenge #2 — network or CIA-triad reasoning. **Still deferred** until WP003 retest passes 2026-05-14.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**6 logged.** *(No new cross-track link from session 8 — password validation is largely a Python-native concept with no clean Bash equivalent. The predicate-proxy lesson IS cross-language but is captured as a WP002-family observation rather than a discrete link.)*

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]`. Bash version is pipe-ready one-shot; Python version composes inside larger scripts.
- *2026-04-28* — **Bash ↔ Python**: frequency analysis. Bash: `... | sort | uniq -c | sort -nr | head`. Python: `Counter(iterable).most_common(N)`. Same gotcha in both: default sort/min/max on numeric strings is lexicographic.
- *2026-04-28* — **Bash ↔ Python**: positional field extraction is fragile. `awk '{print $11}'` and `line.split()[10]` both break when log format shifts. Real fix: regex on value *shape*.
- *2026-05-10* — **Bash ↔ Python**: log line filtering by substring. Bash: `grep "Failed" auth.log`. Python: `with open(path) as f: for line in f: if "Failed" in line: print(line, end="")`. **Asymmetric gotcha:** Python defaults to a `f.readlines()` footgun that Bash `grep` doesn't have because it streams.
- *2026-05-10* — **Bash ↔ Python**: positional field extraction via `.split()[N]` mirrors `awk '{print $N}'`. Python's `.split()` with no args matches awk's default whitespace handling — both reward token-based parsing over byte-based parsing. **Brittleness identical**: index points at wrong field if log format shifts.
- *2026-05-10* — **Python → Bash**: script output captured to file via Bash redirection (`>`). Real triage workflow — Python script extracts/parses; Bash redirection captures output for handoff. Same `>` vs `>>` decision as Evidence Trail Tasks 1 and 2: overwrite for snapshot data, append for accumulation.

---

## 📈 Weekly Summary

**2026-05-05 → 2026-05-11 (rolling 7-day):** 4 sessions, ~370 minutes total (~**6h 10m**). Above 5h target, well below 12h drift threshold. Recovery trajectory holding through the second week. Six challenges completed in this rolling window: Bash L1 Find Tour, Concepts L1 #1, Python L1 #1, Bash L1 Evidence Trail (closes Bash L1), Python L1 #2, Python L1 #3 (today). Next formal weekly summary regenerates 2026-05-15.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box).
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**. Required before any scanning / network challenge. Gates Bash L2 ping sweep and most Python L3 work.
- ✅ `labs/bash-L1/triage/` — reusable; lab contents from Evidence Trail still in place.
- ✅ `labs/bash-L1/retest-wp002/auth-snippet.log` — reusable for 2026-05-12 WP002 retest.
- ✅ `python/L1/` — now contains three scripts: `log_filter.py`, `ip_extractor.py`, `password_audit.py`. Test data for Password Auditor is inline (hardcoded test passwords) — no lab file needed for this challenge type.

---

## 📁 Portfolio Stats

- Write-ups generated: **8** *(↑ from 7 — Password Auditor archived 2026-05-11)*
- Write-ups archived (with reflections filled): **8** *(↑ from 7 — full archive parity, all 8 generated write-ups archived)*
- Total challenges completed: **8** *(↑ from 7)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **8** *(↑ from 7)*
- Total hours: **~8.4** *(↑ from 7.4)*
