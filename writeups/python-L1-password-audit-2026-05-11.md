# Password Auditor

**Track:** Python | **Level:** L1 | **Date Completed:** 2026-05-11 | **Hints Used:** Tier 1 + Tier 2 | **Time Spent:** ~60m

## What This Was

Third Python L1 challenge — first one outside the log-parsing domain. Defines `audit(password)` to evaluate a password against four criteria (length ≥ 12, ≥ 1 uppercase, ≥ 1 lowercase, ≥ 1 digit) and return both a verdict (strong / weak) and a list of named criteria that failed. The caller loops over four test passwords and formats one output line per case. Maps to the policy-enforcement layer of every authentication system — the first defensive layer against credential stuffing and brute-force attacks (the same attack class WP002's auth log was exposing). The shape — _test multiple criteria, return a verdict plus a named failure list_ — generalises to all input validation: form fields, API parameters, file uploads, security headers.

## What I Built

I built a function that checks the strength of a password against 4 criteria. Length, lowercase, uppercase and a digit. The idea is to return whether the password is strong or weak and what conditions failed. So in a real world example the user would understand what failed.

## Key Concepts Used

- **String predicate methods** — `c.isupper()`, `c.islower()`, `c.isdigit()` test a property of a single character and return a boolean. Pure predicates. Different from `c.upper() == c`, which is a _proxy_ that also returns True for any character without case (digits, spaces, punctuation). The proxy trap is the bug class that lets a password like `"abcdef12345678"` falsely satisfy a "must contain uppercase" rule.
- **Don't use proxies for predicates when real predicates exist.** Engineering principle that surfaced here as a real bug. `c.upper() == c` works on common test inputs and silently lies on adversarial ones. **Same family as WP002's broader generalisation** — verify what you claim to verify, not a proxy that doesn't hold under adversarial input. Language-independent lesson.
- **Boolean composition with `and` chain** — `min_12 and one_upper and one_lower and one_digit` short-circuits and returns the composite verdict directly. More Pythonic than `if X == True and Y == True ...`.
- **List as accumulator pattern** — build a list dynamically by appending failure names as they're discovered, rather than constructing a static string with conditional concatenation. Solves three problems at once: the _"without hardcoding"_ question, the brief's required return type, and the trailing-comma bug in string concatenation. **One refactor closes three issues — convergent-fix moment.**
- **Tuple return + tuple unpacking** — `return verdict, failures` returns a tuple; caller writes `result, failures = audit(p)` to unpack into named variables. Pythonic shape for functions returning multiple values; reads cleaner than `result[0]` / `result[1]` indexing.
- **`", ".join(failures)` for delimited output from a list.** Takes a list, stitches with a separator. Handles the empty-list case for free (joining `[]` returns `""`), so the STRONG-case output line doesn't need a special branch. Solves the trailing-comma bug that plagued earlier revisions.
- **Inclusive-bound precision** — _"at least 12"_ means `>= 12`, not `> 12`. Off-by-one errors on length boundaries are a real auth-system bug class. Boundary question caught on `"alllowercase"` (length 12) before submission — verification-instinct moment.
- **Early-break vs micro-optimisation discipline.** Kept the outer break (`one_lower and one_upper and one_digit → break`) because it's a real win on long happy-path inputs. Dropped the per-predicate `and not one_X` guards because the inconsistency across three checks (two without guard, one with) was a worse smell than the work being saved. Engineering principle: optimise for readability first; reach for micro-opts only when profiling data tells you to.

## What I Got Wrong First

I got the functions wrong initially, `.upper()` will return true for a digit even when it shouldn't, but the `.isupper()` function avoids this. Same case for lowercase. I got the return value for the function wrong. I didn't realise I had to return a bool and a list. I also struggled with printing the output.

## Weak Points Flagged

**No new WPs.** Two soft signals:

- **Predicate-proxy bug (`c.upper() == c`) — one-shot self-correction.** Flagged Critical 1 in review 1; self-corrected on revision after a concept nudge ("what's another built-in like `.isdigit()`?"). Single occurrence, lesson landed. Not opening a WP.
- **WP001 evidence note (brief precision).** Brief said _"call on the four test passwords"_; first two submissions called on one. Closed cleanly on revision 3 after an explicit nudge. Soft evidence — needed a prompt to close, not an outright failure. Existing WP001 retest 2026-05-15 still on calendar.

**Cross-track note:** the predicate-proxy lesson is the same shape as WP002's broader generalisation. WP002 covers _"verify what you claim, not a proxy"_; today's bug was that exact pattern in Python. Worth carrying as a language-independent lesson.

## What I Would Do Differently

Next time I would read the question more carefully to make sure I get the output correctly. I would make sure to use `.join()` for joining together a list of strings. I would also need to make sure that there are no logical bugs within the code. Even if it appears to work as expected, there might be hidden bugs.

## Final Solution

```python
def audit(password):
    min_12 = len(password) >= 12
    one_upper = False
    one_lower = False
    one_digit = False
    for char in password:
        if one_lower and one_upper and one_digit:
            break
        if char.isupper():
            one_upper = True
        if char.islower():
            one_lower = True
        if char.isdigit():
            one_digit = True

    output_list = []

    if not min_12:
        output_list.append("length")
    if not one_upper:
        output_list.append("uppercase")
    if not one_lower:
        output_list.append("lowercase")
    if not one_digit:
        output_list.append("digit")


    return min_12 and one_upper and one_lower and one_digit , output_list

test_passwords = ["CorrectHorse9Battery", "Short1A", "alllowercase", "PASSWORD"]

for test in test_passwords:
    result, failures = audit(test)
    output = test + ":"
    if result:
        output += " STRONG"
    else:
        output += " WEAK - failed: "
    output += ", ".join(failures)
    print(output)
```

**Output:**

```
CorrectHorse9Battery: STRONG
Short1A: WEAK - failed: length
alllowercase: WEAK - failed: uppercase, digit
PASSWORD: WEAK - failed: length, lowercase, digit
```
