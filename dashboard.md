# Cybersecurity Training Dashboard
*Last updated: 2026-08-02 — Session 26. **picoCTF pivot** — 8 General Skills flags in one session. loginwatch parked at 10/15. Head-of-Year review (Fable) due 2026-08-06 and speaks first.*

---

## Pickup Here

**RESUME AT — more picoCTF / CyLab General Skills.** User has pivoted to CTF practice and plans to stay there indefinitely (*"im just going to be doing picoCTF for now. dont know when i will stop"*). Queue includes **Printer Shares 2/3**; otherwise his pick.

> ### ⭐ Head-of-Year Review (Fable) — DUE 2026-08-06, SPEAKS FIRST
> Next bootstrap on/after 2026-08-06: spawn a **Fable agent** (`model: fable`) and deliver its review **before** the teacher greets or plans. It should read the **session 24 + 25 + 26** logs — **two of the last three sessions had tutor-side friction** (25 badly; 26 twice-"acting stupid" + a CyberChef yak-shave). Arc questions: is the CTF pivot going well, *and* is teacher-side execution trending wrong? **His pushback on method has been right three sessions running — treat as data, not mood.**

**CTF operating rules (in force):** tool-lookups fine, answer-lookups not · ~30–45 min struggle floor → stuck-report → tiered nudge · describe challenges in his own words · **cold-redo clean solves ~2–4 weeks later** (this batch ~2026-08-22) · write-ups = failure trail + defender's note.

**All CTF work is logged in [external/cylab-notes.md](external/cylab-notes.md)** — per-challenge notes + cold-redos, an **Encoding Recognition cheat sheet**, and a **CyberChef local-setup reference**.

---

## Session 26 (2026-08-02) — picoCTF, 8 flags

Long session, time untracked at his request (~2.5h est). Rung 2 of his practice ladder, running parallel to the parked loginwatch project.

| # | Challenge | Skill | Help needed |
|---|-----------|-------|-------------|
| 1 | ping-cmd | OS command injection (chaining vs substitution) | ~none, solo |
| 2 | bytemancy-0 | `script \| nc` payload piping | solo |
| 3 | Piece by Piece | `cat`-reassemble split files + `unzip` | very stuck (vocab gap) |
| 4 | Sudo Make Me a Sandwich | `sudo -l` → run emacs as root (privesc) | 2 light reframes |
| 5 | Password Profiler | **cupp** OSINT → wordlist → SHA-1 crack | tool-driven |
| 6 | multicode | layered decode b64→b58/62→hex→URL→ROT13 | recognition taught |
| 7 | Log Hunt | `grep\|cut\|sort -u` dedup on the invariant part | help on `cut` |
| 8 | FantasyCTF | ethics/onboarding narrative (integrity choices) | solo |

**⭐ Best win (his, unprompted):** he abstracted a single meta-principle out of five challenges — **"search and read before you act."** `nmap -sV`, `file`, `sudo -l`, and reading the provided `check_password.py` are all the same move: **enumerate before acting.** He named it himself — which is exactly the retention mechanism the whole programme is built to produce (one principle beats five memorised commands). It has a name: **enumeration** — "90% of the work."

**Second win:** on Password Profiler he chose **cupp** (the intended tool) over forcing his half-built Python generator to the line — knowing when *not* to build. Parked his own generator as a project, and spawned a genuinely good **blue-team idea**: invert cupp — reject a signup password if it appears in the wordlist generated from the user's *own* details (aligns with **⚠️ Verify:** NIST SP 800-63B §5.1.1.2, context-specific words). Logged as a candidate `sectools` sibling to loginwatch.

**Retention flag (his own):** after learning `awk '!x[$0]++'` from a writeup he said *"because i didnt use it, i definitely wont remember it."* Correct — it's his core problem. Offered a 90-second drill; he skipped it. **Two application touchpoints remain: the ~2026-08-22 cold-redo and loginwatch Increment 11 (awk).** Don't let Inc 11 pass without making him *type* it.

### 🔴 Tutor-side notes (for the head of year)
Two *"you are acting stupid"* moments: (1) a **false analogy** — claimed he'd run a shell `cut … | sort | uniq -c` pipeline in loginwatch when that CSV work was Python; corrected sharply (verify-before-claiming miss). (2) **over-ran verification** on Log Hunt after he'd already solved and hand-assembled the flag and moved on. Plus a **CyberChef yak-shave** — steered him to a local download (overkill for a CTF string), the `file://` build hung on blocked web workers, fixed by serving it over `python3 -m http.server`. Technical help was sound; I twice added friction he had to push back on. **Third session running where his read on method was right.**

---

## Active Project — `loginwatch` (PARKED at 10/15)

Blue-team auth-log brute-force detector; first portfolio project and the reference template. **No project work this session** — user is on the CTF run. Resumes at **Increment 10 — nonzero exit on findings** (`sys.exit` / exit codes) whenever he returns to building.

- **Repo:** `/home/emrebektas/sectools` — 6 commits through `e25dd91`; dual-role work committed since. **GitHub repo still not created** (open debt).
- **Groundwork for Inc 10:** met exit code `2` from argparse's receiving end at Inc 9. grep precedent — `0`=match, `1`=no-match, `2`=error. Tool currently exits `1` on a bad path (uncaught `FileNotFoundError`), colliding with grep's `1`.
- **Brief format MANDATORY** ([feedback_show_the_path]): every brief states the full structural map up front — files, signatures, data flow, decisions. Withhold the *how*, never the *what-changes*.
- **🌱 Planted lesson at Increment 11 — do not pre-empt.** `report.py` loops over a **set**, so output order flips between runs. It'll fire a **false positive** once `run-daily.sh` diffs day-to-day. Let him build it, let it fire, *then* let him find the cause. **Also at Inc 11: make him actually type `awk '!x[$0]++'`** (read this session, not applied).

| # | Increment | Status |
|---|-----------|--------|
| 0–9 | spec → parse → modules → detect → dual-role → report → CSV → argparse | ✅ |
| — | dual-role IPs into both output formats | ✅ |
| 10 | Nonzero exit on findings (`sys.exit`) | 🔜 next (when project resumes) |
| 11 | `run-daily.sh` (Bash + `$?` + `if` + **awk**) | ⬜ |
| 12–15 | `install.sh` · pytest · packaging · README/MANUAL | ⬜ |

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete; L2 underway via loginwatch (parked 10/15). Tool-building criteria substantially met. |
| Bash | **L2 (pending)** | L1 complete. Bandit (11 levels) + this session's CTF forensics (`grep`/`cut`/`sort`/`uniq`/`awk`) carry real Linux load. L2 proper arrives at loginwatch Inc 11–12. |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks when Python L2 + Bash L2 both complete. |

---

## Active Weak Points

**None.** WP001 retired 2026-07-29; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track. Carried-forward discipline watched quietly inside review: *verify-don't-proxy*.

---

## picoCTF / CyLab — CTF Practice

Rung 2 of the practice ladder (**picoGym/CyLab General Skills**). Self-directed, parallel to the project.

- **Flags captured: 10 total** (bytemancy-1 s22 · Printer Shares · + 8 this session).
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) — stumper notes + cold-redo list. Now also holds an **Encoding Recognition cheat sheet** (base64/32/58/62, hex, ROT13, URL, decimal, binary — identify by character set) and a **CyberChef local-setup reference**.
- **Cold-redo due ~2026-08-22** for this session's batch (Printer Shares was ~2026-08-14).
- **CyberChef** downloaded to `~/cyberchef/`. Relaunch: `python3 -m http.server 8000 --directory ~/cyberchef` → `http://localhost:8000/CyberChef_v11.3.0.html`. (The bare `file://` build hangs on blocked web workers — serve it over HTTP.) Online fallback fine for CTF strings: gchq.github.io/CyberChef.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit11** (ROT13, not started). bandit0→6 cleared 2026-07-24; 6→11 cleared 2026-07-30 (solo, zero hints).
- **Cold-redo:** wipe notes, redo bandit0→6 cold after ~2026-08-07.
- Notes: [external/bandit-notes.md](external/bandit-notes.md) (public, lessons only). Passwords in `overthewire/notes.txt` — gitignored, never committed (verified 2026-07-30).

---

## Open Debts

1. **Ship `sectools` public** — spellcheck SPEC.md + OPSEC scrub + create the GitHub repo + push. *The one standing project debt.*
2. **New parked idea (his):** blue-team password-strength checker that inverts cupp (reject a password derivable from the user's own details — NIST 800-63B). Candidate `sectools` sibling.
3. Vulnerable target VM (Metasploitable2/DVWA) — not needed until end of the project arc.

---

## Checkpoints

- [x] Diagnostic *(2026-04-27)* · Bash L1 *(2026-05-10)* · Python L1 *(2026-05-11)* · Concepts L1 *(2026-05-18)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] 10+ archived write-ups *(2026-05-18)*
- [x] First L2 challenge *(2026-07-18)* · First multi-file Python program *(2026-07-23)*
- [x] First machine-readable tool output *(2026-07-29)* · First real CLI *(2026-07-30)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 10** (8 this session)
- `loginwatch` increments: **10 / 15**
- Bandit levels cleared: **11** (bandit0→11)
- Total sessions: **26** · Total hours: **~26.3**
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- Cross-track connections: **15**
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

Last weekly summary 2026-07-29 (next due ~2026-08-05). Recent cadence is near-daily: sessions 23 (07-29), 24 (07-30), 25 (07-31), 26 (08-02) — comfortably inside the 5–10h band and matching the rhythm he said he wanted.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch 10/15, 6 commits through `e25dd91` + dual-role work, **GitHub repo not yet created**.
- `ctf-work/` — CTF solution scratch, **gitignored** (stays local; keeps public repo clean + cold-redos honest).
- Localhost (`127.0.0.1`) — legal Python socket test target.
