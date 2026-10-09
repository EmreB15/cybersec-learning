# Cybersecurity Training Dashboard
*Last updated: 2026-10-09 — Session 29. **CTF cold-redo audit + the Bandit diversion.** Two overdue redos run (one partial, one fail), Bandit unstuck from 11 to 13 after 70 days, and the session where the tutor was wrong and said so.*

---

## Pickup Here

> ### ⭐ HEAD-OF-YEAR REVIEW DUE **2026-10-14** (Fable)
> If the next session falls on or after that date, the **Fable agent speaks FIRST** — before any greeting or plan. Brief it on: Inc 10 + 13 shipped with 14 tests green (its priority #2, half done), **`sectools` still not public** (the other half, open since July), the cold-redo results below, Bandit unstuck at 13, and the fact that the tutor was corrected on method for the **fifth consecutive session**.

**Recommended plan: `loginwatch` Increment 11 — `run-daily.sh`.** Three reasons: it's the **Bash L2 deliverable**, and Bash L2 + Python L2 is what unlocks Scenarios; it *consumes* the exit-code contract built at Inc 10, which is why Inc 10 came first; and after a CTF/Linux session the project spine is due.

> **🌱 Two planted lessons at Increment 11 — do not pre-empt either.**
> 1. `report.py` loops over a **set**, so output order flips between runs → it will fire a false positive the moment `run-daily.sh` diffs day-to-day. Let him build it, let it fire, *then* let him find the cause.
> 2. Make him **actually type** `awk '!x[$0]++'`. It's already sitting in his Log Hunt notes and has never been used in anger.

**Smaller alternative:** ship `sectools` public — ~10 minutes (spellcheck SPEC.md, OPSEC scrub, create the repo, push). Open debt #1 since July, and there's now materially more worth showing. A `loginwatch` write-up covering the exit-code contract + test suite is also unwritten and is strong portfolio material.

---

## The one thread that matters: **identify before you act**

Both cold redos failed on the **same axis**, and it's now the single tracked thread across the CTF lane.

| Redo | Verdict | What failed |
|---|---|---|
| **Printer Shares** | 🟡 partial pass | smbclient half now **solo** (was fully AI-guided in July). But `nmap -Pn -sV` was **not** his first move — **second time** — he read the webpage hints to learn it was SMB. |
| **Piece by Piece** | 🔴 fail | Reached for `zip` instead of `cat`, looping ~6 commands. **`file` skipped for the third time**, including once when asked for it directly. |

**The intervention was bandit12.** ~9 forced iterations of `file` → read → act. That's the first time the reflex was trained **by repetition** rather than written down as a resolution — and he finished the level essentially solo.

**Requeued, and graded on identification alone regardless of flag capture:**
- **Piece by Piece ~2026-10-23** — `file` first? `cat` not `zip`?
- **Printer Shares ~2026-11-05** — is `nmap -Pn -sV` the **first** command, before any hint or guess?
- **bandit12 ~2026-11-06** — `xxd -r` first? `file` between *every* step?

**Standing reprompt:** on any challenge with an unknown port, `nmap -Pn -sV` is the required first move and the tutor holds him to it.

> ### 📌 TEACHING RULES — all mandatory
> **NEW 2026-10-09 — NO PATTERN WITHOUT EVIDENCE.** Don't assert a trend ("second time tonight") unless the transcript order supports it, and don't close an exchange with an appended moral. Single errors get a one-line fix and no commentary.
> *This one came from the tutor being flatly wrong: his stall at bandit12 was labelled a reading failure, but `hexdump -C` and `hd --help` ran **before** the decompression attempts — he'd engaged with the hexdump correctly and was blocked by not knowing `xxd -r`. A tool gap, not a reading gap. He escalated to "make this mistake again and we done for the night" and he was right on the facts.* Mirrored into Claude Code memory so it survives context loss.
>
> **Carried from session 28:** Implementation mode is the **default** (tutor decomposes into numbered steps, he writes the code, trade-offs decided for him with one line of why). **Explanations capped at ~one screen.** **Before writing any 🔴/🟡, quote the line of my own brief it violates** — else it's a teaching observation. **Stop when he says he's solved it.**
>
> **Fifth consecutive session where his pushback on method was correct. Treat it as a signal, not mood.**

---

## Session 29 (2026-10-08 → 09) — the cold-redo audit

No time lock (*"we arent counting time just moving on to some ctf work"*). Ran past midnight. Opened exactly as the session-28 pickup note specified — CTF, not project. No retests due; head-of-year not due.

| # | Work | Verdict | Help |
|---|------|---------|------|
| 1 | **Printer Shares** cold redo | 🟡 partial | Tier 1 → Tier 2 (found `-L` himself) |
| 2 | **Piece by Piece** cold redo | 🔴 fail | Tier 2 (`zip` → `cat`) |
| 3 | **bandit11→12** — ROT13 via `tr` | ✅ | Tier 2→3→4 on syntax; **tool choice solo** |
| 4 | **bandit12→13** — hexdump + ~9 compression layers | ✅ | Tier 2 on the hexdump; rest solo |

**⭐ The best teaching artefact was an error message that lied about its own cause.** He typed `\\host\shares`; smbclient reported receiving `\hostshares`. **Bash consumed the backslashes before smbclient ever saw the argument** — four in, one out, and the one before `shares` gone. The error was describing a *different string* than the one he typed, which is why it read as nonsense. **Rule banked: when a command rejects an argument as malformed, check whether the shell rewrote it first — the error usually echoes back what actually arrived.**

**⭐ Magic numbers, and they'd been on screen the whole time.** The bandit12 hexdump opened `1f 8b 08` — gzip's signature — with `BZh91AY&SY`, bzip2's, further in. **That is literally how `file` works**: read the leading bytes, look them up in a table of signatures. He'd been staring at the table in raw form while guessing at tools.

**⭐ `split` names its own inverse.** `part_aa part_ab part_ac` is `split`'s *default output naming*. A set of files differing only by a trailing `aa/ab/ac` is a fingerprint, and the inverse of `split` is `cat`. The flag itself said so: `z1p_and_spl1t_f1l3s`.

**Solo wins worth naming:** he picked `tr` out of **six** manned candidates (the hard part); self-corrected `>` to `|` unaided (`>` wants a *filename* — bash tried to create a file called `tr`; `|` wants a *command*); cleaned the junk `.zip` out of the glob path before reassembling, after being warned the trap existed but not walked through it; and built `tr a-zA-Z n-za-mN-ZA-M` with the case halves in **matching order on both sides** — the part that fails silently if reversed.

**Where the `file` reflex stood, honestly: 0 for 3** before bandit12 forced it. Skipped in August, skipped on the redo, and skipped a third time when asked for directly. Writing it down had not worked; repetition did.

**Cross-track link (+1 → 19):** **identify by content, not by label or position.** `file` reads magic numbers and tells the truth; `gzip` dispatches on the **filename extension** and will refuse a genuine gzip file named `.gzip`. Same decision he'd already made as an *author* in Python — replacing `words[-4]` (trust the position) with `words.index("from") + 1` (anchor on a landmark), which fixed the `ip='for'` bug on 2026-10-07. **Security payload:** extension-based trust is an attack surface (`invoice.pdf.exe`, upload filters that accept `.jpg` without reading bytes) — content inspection is the control, labels are attacker-supplied input.

---

## Active Project — `loginwatch` (12/15)

Blue-team auth-log brute-force detector; first portfolio project and the reference template. **Untouched this session by design.**

- **Repo:** `/home/emrebektas/sectools` — 11 commits, clean tree. **GitHub repo still not created** (open debt #1).
- **Contract:** `0` = clean · `1` = findings · `2` = error. In `SPEC.md` **and enforced by tests**.
- **Test suite: 14 passing** — 5 end-to-end exit-code (`subprocess`), 4 detection unit, 5 parser. Mutation-verified.
- **Known gap, logged in the commit message:** `outcome` is still read as `words[5]` — `IndexError` on a short line, junk like `outcome='ssh2'` on a variant one, which **silently drops the event from both detection functions**. Fix is the anchor pattern he already applied to the IP, plus a skipped-line counter so silent drops become visible.

| # | Increment | Status |
|---|-----------|--------|
| 0–9 | spec → parse → modules → detect → dual-role → report → CSV → argparse | ✅ |
| 10 | Nonzero exit on findings + error path (`sys.exit`) | ✅ 2026-10-07 |
| **11** | **`run-daily.sh` (Bash + `$?` + `if` + awk)** | ⬜ **next — recommended** |
| 12 | `install.sh` | ⬜ |
| 13 | pytest with fixtures *(pulled forward)* | ✅ 2026-10-07 |
| 14 | `pyproject.toml` + console entry point | ⬜ |
| 15 | README + MANUAL | ⬜ |

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete. L2 criteria all three demonstrated — argparse (Inc 9), pipeable CSV (Inc 8), `subprocess` (Inc 13). Last active **2026-10-07**. |
| Bash | **L2 (pending)** | L1 complete. Bandit 13 levels + CTF carry real Linux load — this session was heavy on it (`tr`, `xxd`, `tar`, globbing, shell escaping). L2 proper arrives at loginwatch Inc 11–12. Last active **2026-10-09**. |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks when Python L2 + Bash L2 both complete. **Inc 11 is the gate.** |

---

## Active Weak Points

**None.** WP001 retired 2026-07-29; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track.

Watched quietly inside review rather than as a logged weak point: **read the output you were given.** It surfaced twice this session — zip's `adding:` list omitted `part_aa` (the evidence the command had been misunderstood, printed on screen and not read), and `file` said `ASCII text` immediately before a `gzip` attempt. WP002 family. Not opening a weak point on it; the bandit12 repetition was the intervention.

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17** (unchanged — this session's two were re-solves, not new challenges).
- **Cold redos run: 2** (first ever) — Printer Shares 🟡 partial, Piece by Piece 🔴 fail. Both 48–55 days late, both overtaken by the illness gap and then by project momentum. **Lesson for the programme: HIGH-priority redos must not drift 7 weeks.**
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) — tutor-logged this session at his request (*"you can do the logging for me"*), entries labelled as tutor-written so the record stays honest about voice.
- **Still queued:** Sudo Make Me a Sandwich needs one clean **self-powered** re-test (last was Gemini-assisted) · 2026-09-30 batch ~2026-10-21 · 2026-10-03 batch ~2026-10-24 · **Endianness** he self-flagged *"i doubt i will remember this"*.
- **Rules in force:** tool-lookups fine, **answer-lookups not** — tiered nudge from the teacher, not another AI. Describe the challenge in his own words first.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit13** (`sshkey.private`, not started). **Last touched 2026-10-09** — unstuck after 70 days. The diversion push was correct and **bandit12 earned its place in the programme**.
- **Next diversion trigger: 2026-10-16** (7-day rule).
- **Cold-redo still outstanding:** wipe notes, redo bandit0→6 cold (overdue since ~2026-08-07).
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Passwords in `overthewire/notes.txt` — gitignored, never committed.

---

## Open Debts

1. **Ship `sectools` public** — spellcheck SPEC.md + OPSEC scrub + create the GitHub repo + push. ~10 minutes, standing since July, head-of-year priority #2.
2. **Install mypy** — two wrong type hints shipped in session 28 that no test can catch.
3. **`loginwatch` write-up** — none written since July; the exit-code contract + 14-test suite is the strongest portfolio material to date.
4. **Parked idea (his):** blue-team password-strength checker inverting cupp (reject a password derivable from the user's own details — NIST 800-63B). Candidate `sectools` sibling.
5. Vulnerable target VM (Metasploitable2/DVWA) — not needed until the end of the project arc.

---

## Checkpoints

- [x] Diagnostic *(2026-04-27)* · Bash L1 *(2026-05-10)* · Python L1 *(2026-05-11)* · Concepts L1 *(2026-05-18)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] 10+ archived write-ups *(2026-05-18)*
- [x] First L2 challenge *(2026-07-18)* · First multi-file Python program *(2026-07-23)*
- [x] First machine-readable tool output *(2026-07-29)* · First real CLI *(2026-07-30)*
- [x] First Head-of-Year review *(2026-09-30)*
- [x] First automated test suite — 14 tests, mutation-verified *(2026-10-07)*
- [x] First real bug found by his own tests *(2026-10-07 — `ip='for'`)*
- [x] **First cold redos executed and graded honestly** *(2026-10-09 — one partial, one fail)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `loginwatch` public on GitHub
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 17** · **cold redos run: 2** (1 partial, 1 fail)
- `loginwatch` increments: **12 / 15** · **tests passing: 14**
- **Bandit levels cleared: 13** (bandit0→13)
- Total sessions: **29** · Total hours: **~26.3** *(sessions 27–29 untracked)*
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- **Cross-track connections: 19**
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**Weekly summary (first since 2026-07-29):** three touches in the last nine days — 10-03 (solo CTF), 10-07 (project), 10-08/09 (CTF + Bandit). **Frequency is being met.** Volume is unmeasurable: **durations have been null for four consecutive sessions**, so the head-of-year's *frequency over volume* call still can't be evidenced with numbers. **Don't ask him mid-session** — he reacts badly to process overhead. Estimate from the transcript at wrap instead.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1` installed 2026-10-07.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package. The real fix is a virtualenv, which lands at Increment 14.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch 12/15, 11 commits, clean tree, **GitHub repo not yet created**.
- `ctf-work/` — CTF solution scratch, **gitignored**.
- Localhost (`127.0.0.1`) — legal Python socket test target.
