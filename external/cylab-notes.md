# CyLab Academy (picoCTF) — CTF notes & cold-redo log

Practice log for the CyLab Security Academy Challenge Library (formerly picoCTF / picoGym). Play at https://play.picoctf.org (a.k.a. https://cylabacademy.org).

**This file has two jobs:**
1. **Stumper log** — jot what tripped you up, in your own words, so the tutor can pull recurring gaps into teaching.
2. **Cold-redo list** — the real learning is the *repeat*. Every challenge you needed help on is a candidate to redo **cold ~2–4 weeks later**. Note the technique so the redo is a genuine retention check, not a fresh cold encounter.

**How to use:** one entry per challenge — date, name, category, the technique(s) it taught, and whether you needed help (that sets redo priority). Your own words. **No flags or instance passwords pasted.**

**Operating rules:** look up *tools* freely (`man`, "how does X work"); never look up the *answer/walkthrough*. Struggle → platform hints one at a time → tutor tiered nudge. Describe challenges in your own words.

Format: `YYYY/MM/DD  <challenge> [category] — technique(s) learned — needed help? (redo priority: high/med/low)`

---

<!-- entries below -->

2026/08/02  FantasyCTF [General Skills] — story-based ethics/onboarding, no commands — made the "right" (integrity) choices to reach the flag — solo, straightforward (redo priority: LOW — one-time narrative, no technique to redo)

Not a technical challenge — a narrative where you make choices, and the ethical/sensible ones lead to the flag. The two decision points I recalled:
- **How many accounts to sign up with** → answer: **one**. Multiple accounts game the scoreboard / farm hints → this is about **fair play + platform integrity**.
- **"Search for the flag" vs "discover the flag"** → answer: **discover**. Don't look up the answer; earn it. This is **learning integrity** — and it's the exact discipline this whole tutoring program runs on: solve it yourself / stuck-report to the tutor **>** go to another AI for the answer. "Search" = fetch it; "discover" = earn it.

**Takeaway:** the value wasn't the flag, it was the **rules-of-engagement / integrity layer** — play fair, earn the flag. Same family as the CMA/authorisation framing that governs all real practical work (own machine / own VM / written-authorisation lab only).

2026/08/02  Log Hunt [General Skills] — dedupe repeated log lines on the INVARIANT part (not the whole line) — needed help on `cut` mechanics (redo priority: MED-HIGH, cold-redo ~2026-08-22)

**The problem:** flag pieces scattered across a 2348-line log, each on a line like `[timestamp] INFO FLAGPART: <piece>`, repeated with *different timestamps*. `sort | uniq` failed because it compares the WHOLE line — the varying timestamp makes every line unique, so repeats never collapse.

**The key insight:** to dedupe, first strip away the part that VARIES (the timestamp), so each line reduces to just its invariant piece — THEN dedupe. Don't dedupe the noisy lines; dedupe the signal.

**The pipeline (27 repeated lines → 4 unique pieces):**
```
grep 'INFO FLAGPART' server.log | cut -d' ' -f5- | sort -u
```

**`cut` mechanics learned (this was the snag):**
- `cut` needs BOTH `-d` (delimiter) AND `-f` (which fields). `-d` alone errors with "you must specify a list of ... fields". Single dash `-d`, not `--d`.
- `-fN-` = "field N to the end" (onward), vs `-fN` = just field N. Use `N-` defensively in case a piece has a space.
- **Count the fields, don't assume:** `[1990-08-09 10:00:10]` has a space *inside* the brackets, so the timestamp is TWO fields — the piece is field **5**, not 4.

**Two cleaner alternatives (verified — all three give the same 4 pieces):**
- `grep -oP 'INFO FLAGPART: \K.*' server.log | sort -u` — `grep -o` prints only the match, `\K` drops everything before it → no field-counting at all.
- `awk '/INFO FLAGPART/{print $NF}' server.log | sort -u` — `$NF` = last field, direct.

**Reassembly:** `sort -u` returns pieces alphabetically, not in flag order — so lay them out by reading (`picoCTF{` first, `}` last). Manual for 4 pieces.

**CANONICAL UPGRADE (from writeups, verified on the real log):** the flag pieces leak in *chronological* order, which IS flag order — so the elegant solve auto-assembles with **order-preserving dedup** instead of `sort -u`:
```
grep -oP 'INFO FLAGPART: \K.*' server.log | awk '!x[$0]++' | tr -d '\n'
# → picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}   (fully assembled, no manual step)
```
- **`awk '!x[$0]++'` = dedupe WITHOUT sorting** (keeps first-seen order). `x[$0]++` returns this line's seen-count then increments; first time = `0` → `!0` true → print; after = ≥1 → skip. A classic, broadly useful idiom.
- **Rule to bank: `sort -u` when order doesn't matter; `awk '!x[$0]++'` when it does.** `sort` reordered alphabetically and scrambled the flag — that's why I had to reassemble by hand.
- `tr -d '\n'` glues the lines into one string. First real taste of awk associative arrays (→ loginwatch Increment 11).

**Defender's note:** "leaking pieces of a secret in its logs" is a real vuln class — secrets/tokens/PII written into log files (CWE-532). Logs get shipped to aggregators, backups, support tickets — a secret in a log is a secret disclosed. Never log credentials or sensitive values.

**Cold-redo (~2026-08-22):** repeated log lines with a varying field — do I reach for "strip the varying part → `sort -u`" and build the `grep | cut -f | sort -u` pipeline solo, without fighting `cut`'s two-flags requirement?

### 🔧 TOOLING REFERENCE — CyberChef (local, offline)

Downloaded to `~/cyberchef/` (full extraction: HTML + `assets/` + `images/` + `modules/`). **Don't open the HTML as a bare `file://`** — the browser blocks CyberChef's background workers and it hangs forever on the spinning cog loader. **Serve it over a local web server instead:**
```bash
python3 -m http.server 8000 --directory ~/cyberchef
# then open in any browser:
http://localhost:8000/CyberChef_v11.3.0.html
```
Why: over `http://localhost` the browser treats it as a real web origin and allows the workers; `file://` doesn't. **General rule — any local web app that won't run from a bare file: put a tiny HTTP server in front of it.** Online fallback (fine for CTF strings, nothing sensitive): https://gchq.github.io/CyberChef.
Operations are named `From X` (decode) / `To X` (encode). Recipe runs top→bottom, each op feeding the next — stack layers for multi-encoding challenges. `Magic` op = auto-detect (use to *verify* your own guess, not to skip the thinking).

### 🧭 ENCODING RECOGNITION — quick tells (built by hitting them in Password Profiler / multicode, 2026/08/02)

**Identify by CHARACTER SET first, then decode. The tool applies the decoder; the recognition is the skill — that's what makes you fast.**

| What it looks like | Encoding | Decode with |
|---|---|---|
| `A–Z a–z 0–9 + /`, ends in `=` or `==` (padding) | **Base64** | `base64 -d` · From Base64 |
| `A–Z 2–7`, ends in `=` (up to 6 of them → definitely this, not b64) | **Base32** | `base32 -d` · From Base32 |
| alphanumeric, **no** `0 O I l` (those are dropped) | **Base58** | From Base58 (no coreutils tool) |
| alphanumeric **including** `0 O I l`, no `+ / =` | **Base62** ⚠ non-standard alphabets — decode may need the right alphabet set | From Base62 |
| only `0–9 a–f`, even length, reads as byte pairs | **Hex** | `xxd -r -p` · From Hex |
| letters look shifted; `cvpbPGS` → `picoCTF` is the giveaway | **ROT13** (letters ONLY) | From ROT13 — **rotate-numbers OFF** |
| `%` followed by two hex digits (`%7B`) | **URL / percent** — each `%XX` = one char (`%7B`={, `%7D`=}) | From URL / URL Decode |
| space-separated numbers, each ≤255 | **Decimal** (ASCII char codes) | From Decimal |
| `01000110 …` in groups of 8 | **Binary** | From Binary |

**Cross-cutting rules that saved this solve:**
- **Garbage / mojibake out = WRONG decoder.** A correct peel always reads as clean ASCII (the next layer). Never accept "the answer looks weird."
- **Layers step on each other.** ROT13 chewed the letters inside `%7B`/`%7D` → decode order matters: URL-decode the braces *before* ROT13 so they're no longer letters.
- **ROT13 is letters only** — digits in a flag are literal; rotating them corrupts the flag.
- **Peel until it reads like a flag.** If it isn't plainly `picoCTF{…}`, it's another layer in disguise.



2026/07/31  Printer Shares [General Skills] — SMB share retrieval via `smbclient`; identifying an unknown service with `nmap -sV` — needed full guidance on the solve (redo priority: HIGH, cold-redo ~2026-08-14)

**The actual lesson (bigger than this challenge): don't guess a service from the challenge title — ask the port what it is.**

```bash
nmap -Pn -sV -p <PORT> <host>
```
- `-Pn` — skip host discovery. picoCTF (and most internet targets) ignore ping probes, so without this nmap decides the host is "down" and never scans. This is why my first attempt looked hung.
- `-sV` — service/version detection. Connects, prods the service, fingerprints it. This is the whole point — it turns "no idea what this is" into a named service + version.
- `-p <PORT>` — the port. Fresh instance = fresh port.

Output that solved it: `open  netbios-ssn  Samba smbd 4.6.2` → that's SMB → use `smbclient`, not `nc`. `nc` only works when a service speaks plain text; SMB is structured binary, so it needs a client that speaks the protocol.

**Why nc was a dead end:** `nc -vz` only tells you a port is open (`-z` sends no data by design). An open port is a *service*, and services need their own client.

**The four SMB commands (learn these with time — the priority is the nmap reflex above):**
```bash
smbclient -L <host> -p <PORT> -N              # list shares (-N = anonymous, no password)
smbclient //<host>/shares -p <PORT> -N        # connect to the 'shares' share
#   then at the smb:\> prompt:  ls  →  get flag.txt  →  exit
```

**Honest note:** rated Easy, and it is — *once you know SMB exists*. You can't reason from "printer" to "Windows file-sharing protocol" from first principles; you either know it or you find it with `nmap -sV`. Knowledge gap, not a reasoning failure.

**What was mine vs guided:** the flag was fully guided by another AI. But on a FRESH instance afterward I ran `nmap -sV` blind (no title hint) and identified Samba/SMB myself. That half is the transferable skill. Redo the whole thing cold in 2-4 weeks; the real test is whether `nmap -Pn -sV` is my first move on any unknown port.

**Next:** Printer Shares 2 and 3 (same server, harder — 2 adds credentials, 3 goes further).

---

2026/08/02  ping-cmd [General Skills] — OS command injection (operator chaining + substitution) — barely any help, effectively solo (redo priority: LOW, cold-redo ~2026-08-22)

**The vulnerability:** the server takes an IP and builds a shell command out of it — `ping <your input>`. Because my input is glued straight into a shell string, I can break out of the ping argument and run my own commands. That's OS command injection.

**What I did:** `nc host port` (no `-z`) dropped me into a live prompt asking for an IP. Used `&&` first to confirm the flag file was there (recon), then `;` to `cat` it (payload). Recon-then-payload — picked each operator for what it does, didn't spray all four.

**The four injection operators — and the split that matters:**
```
;        run a second command, unconditionally         →  ping x; cat flag
&&       run the second only if the first succeeds      →  ping x && cat flag
|        pipe ping's output into the next command       →  ping x | grep flag
` `/$()  command SUBSTITUTION — run inner, drop its     →  ping $(cat flag)
         OUTPUT into ping's argument
```
- `;  &&  |` **chain a separate command** onto ping.
- Backticks / `$()` are a **different mechanism** — substitution. The inner command runs and its *output* becomes part of ping's argument (e.g. `ping $(cat flag)` makes ping try to resolve the flag text and often echoes it in the error). **This matters because filters that strip `;&&|` frequently miss `$()`** — it's the fallback when the obvious operators are blocked.

**Correction to bank (I had this wrong in the moment):** the tell that a service is *interactive* (I can talk to it) vs *scan-only* is **`-z`, not `-v`**.
- `-z` = zero-I/O mode: nc opens the port and sends **nothing** — this is what made Printer Shares a dead end (open port, no conversation).
- plain `nc host port` (no `-z`) = a **live two-way channel**.
- `-v` is only verbosity (connection chatter) — it doesn't change whether there's a conversation.

**Vocabulary looked up vs solved:** looked up *only* "what are the common command-injection operators" (an AI refused, so I searched the class of technique). Applied it to the challenge myself. Same as the SMB lookup in Printer Shares — looked up *what the thing is*, worked out *what to try* solo.

**Defender's note:** the bug is building a shell command from untrusted input. The fix is **not** a blocklist of `; && | \` $` — those get bypassed (that's exactly what substitution is for). The real fixes: don't invoke a shell at all (pass an argument array, e.g. `subprocess.run(["ping", ip])`), or strictly validate the input is a real IP before it goes anywhere near a shell. Same trap I'll be on the *other* side of when `run-daily.sh` starts shelling things out.

**Cold-redo test (~2026-08-22):** on a fresh instance, is my first move to check whether the input is fed to a shell, and do I reach for `$()` if the obvious operators are filtered?

---

2026/08/02  bytemancy-0 [General Skills] — script a payload and pipe it into nc — solo, easy (had already done bytemancy-1) (redo priority: LOW)

**The pattern (the actual transferable skill):** when a service wants input that's too long or too fiddly to type by hand, you don't type it — you generate it with a script and **pipe the script's stdout straight into the connection**:
```
python3 bytemancy-0.py | nc host port
```
Python builds the payload (its job); nc carries it over the socket (its job). Two tools, one seam — the same stdout-as-a-pipe idea from Bash. bytemancy-1 was the same move at scale (1751 bytes); bytemancy-0 is 3.

**Idiom to bank:** to emit a repeated character, `print("e" * 3)` (string multiplication) says the intent in one line — a `for` loop over `range(n)` printing one char per pass does the same thing but reads as "I'm counting" rather than "I want N copies." Both correct; the multiplication is the Python-native way to say "repeat".

**Redo note:** near-instant now, so low priority — but the pattern (`script | nc`) is worth keeping fluent because it's the answer to every "send crafted/large input to a service" challenge, not just this one.

---

2026/08/02  Piece by Piece [General Skills] — reassembling split files with `cat`, then `unzip` — was very stuck, needed help (redo priority: HIGH, cold-redo ~2026-08-22)

**The challenge shape:** the archive was split into multiple pieces. The job is to join them back into one file and extract it. The confusing part was recognising they *were* pieces of one thing.

**Reassemble → identify → extract:**
```
cat piece1 piece2 piece3 > combined.zip    # ORDER MATTERS — pieces must go in sequence
file combined.zip                           # confirm it's actually "Zip archive data" first
unzip combined.zip                          # extract
```
- `cat` = **conCATenate**. Its original job is joining multiple files into one stream; the `cat file` I've used to *view* files is just the one-argument case. This is Bash L1 knowledge (`cat` + `>`) doing what it was named for — not new magic.
- If pieces are named sortably (zero-padded, e.g. `part.001 part.002`), a glob works: `cat part.* > combined.zip`.
- **The reflex I skipped:** `file` on a mystery piece tells me what I'm holding — same "ask the thing what it is" move as `nmap -sV` (Printer Shares) and `file` in Bandit. Should have been my first move.

**ssh, banked:** `ssh user@hostname -p portnumber` — lowercase `-p` for the port on ssh (scp uses uppercase `-P`). Password prompt won't echo as you type; first connect asks yes/no to trust the host key.

**Why I got stuck / the honest bit:** didn't know `cat` joins files or that `unzip` exists, and went to an AI for the answer instead of giving the tutor a stuck-report. Next time: 30-min floor → stuck-report → tiered nudge, so the solve stays mine.

**Defender's note:** splitting a file is a real evasion — an AV/DLP scanner that checks each piece on its own sees nothing malicious; the payload only exists once the pieces are reassembled. Scan-on-write tools that don't reassemble miss it.

**Cold-redo (~2026-08-22):** given a pile of numbered/mystery files, is my first move to `file` them, suspect reassembly, and `cat`-in-order → `unzip` — solo this time?

---

2026/08/02  Sudo Make Me a Sandwich [General Skills] — sudo privilege escalation via an allowed interactive binary (emacs) — needed 2 light tutor reframes (redo priority: MED, cold-redo ~2026-08-22)

**The setup:** ssh in as `ctf-player`; `flag.txt` is owned by root and readable only by root, so `cat flag.txt` and `sudo cat flag.txt` both fail (cat isn't a permitted sudo command).

**The escalation path:**
```
sudo -l                    # FIRST MOVE when escalating — lists what I may run as root
# → (ALL) NOPASSWD: /bin/emacs    means: run emacs as ANY user (incl. root), no password
sudo emacs flag.txt        # emacs now runs AS ROOT → can read the root-only file → flag
```

**The core concept (the bit that transfers):** a running program has the permissions of **whoever it runs as**, not permissions of its own. `emacs flag.txt` runs as *me* → denied. `sudo emacs flag.txt` runs as *root* → allowed. sudo changed *who emacs was*, not *what emacs is*. Privilege = the identity of the running process.

**Why plain `emacs` fails:** the file is root-only, and emacs launched by me inherits *my* permissions — it can't read what I can't read. The `sudo` is the whole trick.

**Defender's note:** allowing sudo on an *interactive* binary = handing over full root. emacs (also `vim`, `less`, `more`, `find`, `awk`) can open ANY root file or spawn a root shell — so "let them edit one file as root" silently becomes "let them be root." Scope sudo to single-purpose, non-interactive commands only. The reference attackers use for these breakouts is **GTFOBins** (a tool/reference, not a walkthrough) — auditing your own sudoers against it is a blue-team task.

**Cold-redo (~2026-08-22):** shell as a low-priv user + a root-only file — is my first move `sudo -l`, and do I recognise an allowed interactive binary as a straight route to root, solo?

---

2026/08/02  Password Profiler [General Skills] — **cupp**: OSINT → custom wordlist → SHA-1 crack — tool-driven solve, tutor-guided pipeline (redo priority: MED, cold-redo ~2026-08-22)

**THE CRUX — cupp (Common User Passwords Profiler):** the red-team tool that turns a target's personal details into a custom password wordlist. This whole challenge is built around it — the provided `check_password.py` even says so in a comment (`# wordlist that was generated using CUPP`).

**The pipeline (what the challenge actually hands you):**
1. **Given:** `hash.txt` (the target SHA-1), a userinfo file (the OSINT — personal details already gathered *for* you), and `check_password.py` (the checker, pre-written).
2. **The checker does the cracking FOR you** — it reads `hash.txt`, loops every line of `passwords.txt`, SHA-1s it, compares. Match → prints `picoCTF{<password>}`. So my ONLY job was to produce `passwords.txt`.
3. **Generate `passwords.txt` with cupp:**
```
git clone https://github.com/Mebus/cupp.git
python3 cupp.py -i          # interactive — asks name, nickname, birthdate, partner, pet, company...
                            # answer from userinfo — WHICH details I feed = the OSINT judgment = the skill
mv <name>.txt passwords.txt # cupp names the file after the target; move it next to the checker + hash.txt
python3 check_password.py   # → flag
```

**cupp mangling prompts:** add keywords / special-chars-at-end / random-numbers-at-end / **leet mode**. **Start lean** (leet off), run the checker; add a rule only if it misses. Leet only *adds* candidates — can't lower the hit-rate, the only cost is a bigger file, and SHA-1-ing even a huge list takes seconds. Failure-first: let a miss tell me which rule I need.
**Prompt-decision rule (durable):** a prompt about **words** (keywords/chars/numbers/leet) changes the list — think about it. A prompt about **print/speed/display** doesn't affect the checker — pick anything.

**Core concept — bank this:** it is NOT SHA-1 being weak that cracks it — it's the **password being guessable**. The same attack works on SHA-256. When the password is derivable from public personal info, the hash algorithm barely matters. **The vulnerability is human password choice.**

**Defender's note + spin-off project idea (PARKED):** invert the engine → blue-team. At signup, generate the attacker's wordlist from the user's *own* details; if their chosen password is in it, reject it. Personalised strength-checking — catches `Rex1998!` where a generic meter waves it through. ⚠️ **Verify:** NIST SP 800-63B §5.1.1.2 recommends exactly this — block "context-specific words" incl. username + derivatives (https://pages.nist.gov/800-63-3/sp800-63b.html). Candidate `sectools` sibling to loginwatch.

**Python touched (then parked my own build):** `hashlib.sha1(s.encode()).hexdigest()` — hashes bytes not str, so `.encode()` a variable (`b"..."` is only for literals); `itertools.permutations(list, n)` for ordered combinations; `list(dict.values())`. My generator `password_list_gem.py` reached parse + permutations before I switched to cupp — parked as the "build my own cupp" red-team project.

**Cold-redo (~2026-08-22):** fresh instance — do I recognise "custom wordlist from personal info" → reach for cupp → feed the OSINT → point the checker at its output, solo?

**MY BIGGEST TAKEAWAY (across the whole session, not just this challenge):** sometimes the answer is a lot easier than you think — spend time **searching and reading first**, before jumping into building something. Reading the provided `check_password.py` up front would have shown me the checker was already written and that cupp was the intended tool — I'd have skipped the build-my-own-generator detour entirely. This is the same reflex as `nmap -sV`, `file`, and `sudo -l` from today: **enumerate/read before you act.** In pentest terms this is the *enumeration* phase — "enumeration is 90% of the work." Step zero of any challenge: read everything you were given.
