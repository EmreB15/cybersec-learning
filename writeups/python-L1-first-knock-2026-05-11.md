# First Knock — Single-Port TCP Availability Check

**Track:** Python | **Level:** L1 | **Date Completed:** 2026-05-11 | **Hints Used:** Tier 1 only | **Time Spent:** ~30m

## What This Was

First Python challenge to touch the `socket` module. Build a single-port TCP availability primitive — given a host and port, return True if something is listening, False if not. The same primitive every port scanner is built on top of: L2's full scanner is this function repeated across a port range with concurrency. Closes Python L1 (4/4 challenges done, second track to clear the level after Bash L1).

## What I Built

I built a port scanner that checks if a port is open or closed. Closed can mean many things from errors to just being closed. It loops through some ports and prints out whether they are open or not. I used localhost to open port 8080.

## Key Concepts Used

- `socket.create_connection((host, port), timeout)` — TCP connection attempt as a port-state probe
- Exception handling as control flow: success path returns True, except branch returns False
- `OSError` as the parent class covering all socket-level connection failures (PEP 3151) — `ConnectionRefusedError`, `TimeoutError`, `ConnectionResetError`, `socket.gaierror`
- Resource cleanup: closing the socket on the success path
- Timeout argument to bound the wait on filtered/unreachable ports

## What I Got Wrong First

I initially used a `TimeoutError` but I did not think that other errors could be thrown. I learnt that the parent error here is `OSError`; if you except that, it will cover all socket errors. When I saw a closed socket I saw a timeout error, so I thought it was the only one but I was wrong.

## Weak Points Flagged

- **No new WPs opened.** The narrow-exception bug was caught and corrected in revision.
- **WP002 cross-language evidence (third instance):** "trust the one observation without probing the class" — bash sort-column → python predicate-proxy → python exception-class. Pattern is durable across language. Strengthens WP002's broader description.
- **WP001 positive signal:** brief enumerated two test calls; both exercised without nudge.

## What I Would Do Differently

Next time, when I want to know what something returns and the documentation is confusing, I'll just print it out and actually see what it is. Take it a step further before asking for help.

## Final Solution

```python
import socket


def check_port(host, port, timeout=1.0):
    try:
        socket_1 = socket.create_connection((host, port), timeout)
    except OSError:
        return False
    socket_1.close()
    return True

ip = "127.0.0.1"
ports = [8080, 9999]
for port in ports:
    if check_port(ip, port):
        print(ip + ":" + str(port) + " - OPEN")
    else:
        print(ip + ":" + str(port) + " - CLOSED")
```

**Test setup:**

- Second WSL terminal: `python3 -m http.server 8080` (creates a listener on 8080)
- This terminal: `python3 python/L1/port_check.py`

**Output:**

```
127.0.0.1:8080 - OPEN
127.0.0.1:9999 - CLOSED
```
