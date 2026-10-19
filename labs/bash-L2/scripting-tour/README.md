# Bash scripting tour — teaching demos, session 34 (2026-10-19)

Written by the tutor, not by Emre. These are *not* challenge solutions — each one
demonstrates language machinery in a domain unrelated to the task it was teaching
toward (loginwatch increment 11, `run-daily.sh`).

| Script | Teaches | Run it |
|---|---|---|
| `tour.sh` | variables, `$1`, `$?`, `>&2`, `exit N` — all five, numbered and labelled | `./tour.sh /etc/apt` then `./tour.sh /nope/nothing` |
| `clobber.sh` | why `$?` must be captured on the *very next* line: any command, `echo` included, replaces it | `./clobber.sh` |
| `usercheck.sh` | the whole wrapper pattern — run a tool, read its code, report it, propagate it | `./usercheck.sh root` then `./usercheck.sh nosuchuser` |

To see the stream split, keep the buckets apart:

    ./tour.sh /nope/nothing > out.txt 2> err.txt ; echo "exit=$?" ; cat out.txt ; cat err.txt

`ls` and `grep` both put results on stdout and complaints on stderr without being
asked. That convention is why `run-daily.sh` must not print anything of its own to
stdout.
