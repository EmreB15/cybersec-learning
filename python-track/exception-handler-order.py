"""
How Python picks an except handler.  Runnable reference - `python3 exception-handler-order.py`

THE RULE
  1. Handlers are checked in the order they are written, top to bottom.
  2. The FIRST one that matches runs.  Matching means: is the raised exception
     this class, or any subclass of it?
  3. Exactly ONE handler runs.  After it finishes, execution jumps to the code
     after the whole try statement - the remaining handlers are never consulted,
     whether that block returned, exited, or just fell off the end.
  4. If no handler matches, the exception propagates OUT of the function to
     whoever called it.
"""


# ---------------------------------------------------------------------------
# CASE 1 - unrelated handlers.  ValueError and KeyError share only Exception,
# so no single exception can match both.  Order is irrelevant.
# ---------------------------------------------------------------------------
def case_1(raise_this):
    try:
        raise raise_this("boom")
    except ValueError:
        return "ValueError handler"
    except KeyError:
        return "KeyError handler"


# ---------------------------------------------------------------------------
# CASE 2 - OVERLAPPING handlers, specific first.  This is the correct order.
# FileNotFoundError is a subclass of OSError, so a missing file matches BOTH.
# The specific handler is listed first, so it wins and the useful message survives.
# ---------------------------------------------------------------------------
def case_2(raise_this):
    try:
        raise raise_this("boom")
    except FileNotFoundError:
        return "specific: that file does not exist"
    except OSError:
        return "general: that path exists but could not be read"


# ---------------------------------------------------------------------------
# CASE 3 - the same handlers, flipped.  THIS IS A BUG.
# OSError matches everything the specific handler would have caught, so the
# FileNotFoundError block below it is dead code that can never run.
# ---------------------------------------------------------------------------
def case_3(raise_this):
    try:
        raise raise_this("boom")
    except OSError:
        return "general: that path exists but could not be read"
    except FileNotFoundError:
        return "specific: that file does not exist   <- UNREACHABLE"


# ---------------------------------------------------------------------------
# CASE 4 - one block for several unrelated exceptions: use a tuple.
# ---------------------------------------------------------------------------
def case_4(raise_this):
    try:
        raise raise_this("boom")
    except (ValueError, KeyError):
        return "tuple handler caught it"


# ---------------------------------------------------------------------------
# CASE 5 - no handler matches, so it propagates out to the caller.
# This is what killed the loginwatch scan: ValueError and IndexError escaped
# parse_file's `except MalformedLoginLine` and took the whole program with them.
# ---------------------------------------------------------------------------
def case_5_inner():
    try:
        raise TypeError("boom")
    except ValueError:
        return "ValueError handler"
    except KeyError:
        return "KeyError handler"


def case_5_outer():
    try:
        return case_5_inner()
    except TypeError:
        return "escaped the inner handlers, caught out here"


# ---------------------------------------------------------------------------
# A handler that falls through still blocks the ones below it.
# Nothing returns or exits here - handler 2 is still never reached.
# ---------------------------------------------------------------------------
def case_6():
    trace = []
    try:
        raise FileNotFoundError("boom")
    except FileNotFoundError:
        trace.append("handler 1 ran (no return, no exit)")
    except OSError:
        trace.append("handler 2 ran")
    trace.append("code after the try statement")
    return trace


if __name__ == "__main__":
    print("CASE 1  unrelated handlers - order does not matter")
    print("   raise KeyError   ->", case_1(KeyError))
    print("   raise ValueError ->", case_1(ValueError))

    print("\nCASE 2  overlapping, specific first  (CORRECT)")
    print("   raise FileNotFoundError  ->", case_2(FileNotFoundError))
    print("   raise IsADirectoryError  ->", case_2(IsADirectoryError))

    print("\nCASE 3  overlapping, general first  (BUG)")
    print("   raise FileNotFoundError  ->", case_3(FileNotFoundError))
    print("   raise IsADirectoryError  ->", case_3(IsADirectoryError))

    print("\nCASE 4  tuple handler")
    print("   raise KeyError   ->", case_4(KeyError))
    print("   raise ValueError ->", case_4(ValueError))

    print("\nCASE 5  no match - propagates to the caller")
    print("   raise TypeError  ->", case_5_outer())

    print("\nCASE 6  a handler that falls through still blocks the rest")
    for step in case_6():
        print("  ", step)
