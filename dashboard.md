# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-05-10 — after Session 6 (Concepts L1 #1 + Python L1 #1 both complete; two stale tracks reactivated; WA002 promoted, WP004 logged)*

---

## 🎯 Pickup Here

**Next session: 4 retests due before any new content, in priority order.**

> 📌 **Retest queue (priority order):**
> 1. **WP002 — due 2026-05-12** *(bash frequency-count discipline; failures = 1, stage 0; **third failure triggers a remediation challenge** — highest-stakes retest)*
> 2. **WP003 — due 2026-05-14** *(concepts phishing analysis; verification-habit on a NEW phishing email — fresh email needed, prepare in advance)*
> 3. **WP004 — due 2026-05-14** *(python file iteration; needs a challenge that exposes a real or simulated large-file scenario so the readlines footgun is visible, not theoretical)*
> 4. **WP001 — due 2026-05-15** *(cross-track instruction precision; stage 1 → 2 if pass)*

> 🗺️ **After retests — user picks new content from:**
> - **Bash L1 redirection close-out** (still outstanding — single-concept challenge on `>`, `>>`, `2>`, `2>&1`; lab `labs/bash-L1/triage/` reusable).
> - **Python L1 #2** — string parsing on log lines (extract IPs from Failed entries; addresses diagnostic-flagged shaky string handling).
> - **Concepts L1 #2** — likely network/CIA reasoning scenario; **defer until WP003 retest passes** to avoid stacking.

> 🔧 **Tutor process — confirmed in effect, plus two new notes from session 6:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. **NEW (2026-05-10):** When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*. (Phishing Anatomy lens 1 missed because the framework didn't name the verification-habit move.)
> 6. **NEW (2026-05-10):** When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."* (User assumed DocuSign was made up.)

**Side tasks still open (portfolio polish):**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | L1 | █░░░ 1/4 | 1 | 🟢 Active — first L1 challenge done cleanly |
| 🖥️ Bash | L1 | ███ 3/3 | 3 | 🟡 Challenges met; **redirection still required** to close level |
| 🔐 Concepts | L1 | █░░ 1/3 | 1 | 🟢 Active — first L1 challenge done with redo |
| 🎭 Scenarios | — | Locked | 0 | 🔒 |

**Bash L1 completion criterion:** *3 challenges done + redirection covered.* Challenges-done bar met; redirection bar not. **One more challenge needed**, redirection-focused.

---

## 📝 Session 6 Summary (2026-05-10)

### ✅ Concepts L1 #1 — Phishing Anatomy (DocuSign signature request)

- **6-lens framework introduced** (Sender / Subject / Body / Call to Action / Links / Footer) with sources cited (NIST SP 800-177 Rev. 1; CISA *Recognize and Report Phishing*).
- **First pass — strong on lenses 2/3/4**: caught urgency framing, generic salutation, the disarming *"safely ignore"* line as a deliberate vigilance-lowering tactic (unprompted), and the credential-replay attack pattern (unprompted).
- **First pass — missed lens 1, partial lens 5, abandoned lens 6.** Same pattern as the diagnostic — partial inventory, skipped systematic checks on less-obvious indicators.
- **Tutor framing-error caught mid-review:** original feedback implied prior brand knowledge ("you should have known DocuSign uses .com"). User pushed back legitimately. Reframed: the lens demands verification habit (look it up or name the gap), not prior knowledge.
- **Redo landed:** lens 1 caught domain mismatch + organisational-coherence insight (security-team-as-sender = phishing trope, beyond what the framework asked for); lens 5 hypothesised on .tk (wrong fact — .tk is Tokelau ccTLD, not "tokens" — but right behaviour: name the gap rather than skip the lens); summary sentence added.
- **Lens 6 closed cleanly after walk-through:** "no footer, no copyright line, no legal disclaimer" — got the absence-as-indicator principle.
- **WA002 promoted to WP003** (concepts; method gap, not knowledge gap; retest 2026-05-14).

### ✅ Python L1 #1 — Log Line Reader (`log_filter.py`)

- **Scope-tight challenge, one new concept** (`with open(...) as f:` context manager). 4 lines of code, one job. Output: 27 Failed lines correctly extracted from synthetic auth log; 3 Accepted lines correctly excluded.
- **Scope discipline held throughout** — no count, no IP filter, no formatting embellishment despite open-ended objective.
- **First version had two issues**, both flagged in review and self-corrected on revision:
  - `for line in f.readlines():` (eager full-file load — production-scale footgun).
  - `print(line)` produced double-spaced output (line had `\n`, print added another).
- **Final:** `for line in f:` + `print(line, end="")`. Identical correct output, idiomatic + memory-safe.
- **WP004 logged** on the readlines pattern (retest 2026-05-14 — needs a challenge with a large or unknown-size file so the footgun is visible).
- **Cross-track link logged (4th total):** Bash `grep "Failed" file` vs Python `with-open + for-line + if-in + print`. Same filter, different machinery, different reuse profile.

### 🔧 Tutor process notes captured for next briefs

Both surfaced organically during the session:
1. **Brief-framing on analysis frameworks:** Phishing Anatomy framework said "compare display domain to actual domain" without telling the user what to do when they don't know the actual domain. The lens skill is verification habit — needed in the brief, not surfaced via review correction.
2. **Brand-context for impersonation challenges:** Used DocuSign without naming it as a real B2B SaaS. User assumed it was fictional. Should preface unfamiliar real-world brands with one-line context.

Neither saved as new durable feedback memory — both are restatements/refinements of existing memories (`brief_explicitness`, `audit_as_you_go`).

**Stale-track watch defused:** Both Python and Concepts reactivated before tripping the 14-day flag (2026-05-11).

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters | 1 | 0 | **2026-05-15** |
| WP002 | bash | Frequency-count pipelines: skips count-column sorting, trusts pipeline output without inspecting intermediate stages | 0 | **1** | **2026-05-12** |
| **WP003** | **concepts** | **Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step the lens requires (method gap, not knowledge gap)** | **0** | **0** | **2026-05-14** |
| **WP004** | **python** | **File iteration defaults to `f.readlines()` (eager, full-file load) instead of iterating the file object directly (lazy). Crashes on production-scale logs.** | **0** | **0** | **2026-05-14** |

**Cross-track pattern note:** WP002 (bash, skip-the-inspection-step), WP003 (concepts, skip-the-verification-step), and the lens-5 first-pass behaviour on Phishing Anatomy may all be the same underlying habit — *infer the answer without doing the named verification step*. Watching whether retest data confirms this.

**WP001 retest history:**
- 2026-05-08 — passed cleanly. Brief Precision: 3 sub-tasks, all parameters exactly as briefed, single-tool answers.

**WP002 retest history:**
- 2026-05-08 — failed. Frequency Recall: correct answer surfaced but missed `Failed`-only filter and intermediate inspection (both explicit brief criteria).

> ℹ️ **WP002 description updated 2026-05-08.** Earlier evidence of *"`sort -r` would misrank counts ≥10"* was empirically falsified — `uniq -c` column padding preserves numeric order under lex sort on the raw pipeline. The trap only fires if leading whitespace is stripped (e.g., post-`awk` processing). The round-1 bug from Trail in the Logs (no count-column sort at all) remains real and earned.

---

## 👀 Watch-Areas

*None active.* WA002 promoted to WP003 on 2026-05-10. WA001 promoted to WP001 on 2026-04-28.

---

## 📅 Retests Scheduled

| Date | Weak Point | Track | Stage | Failures |
|------|-----------|-------|-------|----------|
| **2026-05-12** | WP002 (frequency-count pipelines) | bash | 0 | 1 *(third failure → remediation challenge)* |
| **2026-05-14** | WP003 (phishing verification habit) | concepts | 0 | 0 |
| **2026-05-14** | WP004 (python file iteration) | python | 0 | 0 |
| **2026-05-15** | WP001 (instruction-precision) | cross-track | 1 → 2 if pass | 0 |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour; trust-break arc closed)*
- [x] **All three core tracks active at L1** *(2026-05-10 — Python and Concepts both have first L1 challenge done)*
- [ ] All tracks reach Level 1 complete
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups

---

## 🗺️ Up Next

**Bash:** Final L1 challenge — redirection-focused, single-concept (`>`, `>>`, `2>`, `2>&1`). Closes Bash L1.
**Python (L1):** Challenge #2 — string parsing on log lines (extract IPs from Failed entries). Direct sequel to log_filter.py + addresses diagnostic-flagged shaky string handling.
**Concepts (L1):** Challenge #2 — network or CIA-triad reasoning scenario. **Defer until WP003 retest passes** to avoid stacking.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**4 logged.**

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]` or `[-N:]`. Bash version is a pipe-ready one-shot; Python version composes inside larger scripts.
- *2026-04-28* — **Bash ↔ Python**: frequency analysis. Bash: `... | sort | uniq -c | sort -nr | head -n N`. Python: `collections.Counter(iterable).most_common(N)`. **Same gotcha in both**: default sort/min/max on numeric strings is lexicographic. Convert to int first.
- *2026-04-28* — **Bash ↔ Python**: positional field extraction is fragile. `awk '{print $11}'` and `line.split()[10]` both break when log format shifts. Real fix: regex extraction targeting value *shape*.
- *2026-05-10* — **Bash ↔ Python**: log line filtering by substring. Bash: `grep "Failed" auth.log`. Python: `with open(path) as f: for line in f: if "Failed" in line: print(line, end="")`. **Asymmetric gotcha**: Python defaults to a footgun (`f.readlines()` materialises the whole file in memory) that Bash `grep` doesn't have because it streams. Decision factor: one-shot check vs reusable building block.

---

## 📈 Weekly Summary

**2026-05-04 → 2026-05-10:** 2 sessions, ~160 minutes total (~2h 40m). **Below the 5h target** but on a recovery trajectory — last week was 70min, this week is 160min. Concepts L1 #1 + Python L1 #1 + Bash L1 Find Tour all completed in the window.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box).
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — not yet installed. **Required before any scanning / network challenge.**
- ✅ `labs/bash-L1/triage/` verified clean *(8 files, mtimes intact)*. Reusable for redirection challenge.
- ✅ `labs/bash-L1/retest-wp002/auth-snippet.log` reused 2026-05-10 as data source for Python L1 #1; reusable again for next WP002 retest 2026-05-12.

---

## 📁 Portfolio Stats

- Write-ups generated: **5** *(↑ from 3)*
- Write-ups archived (with reflections filled): **5** *(↑ from 4 — all generated write-ups archived; bash-L0-first-footprints archived 2026-05-10 in session 7)*
- Total challenges completed: **5** *(↑ from 3)*
- Total challenges attempted-unfinished: 2
- Total sessions: **6** *(↑ from 5)*
- Total hours: **~5.4** *(↑ from 3.9)*
