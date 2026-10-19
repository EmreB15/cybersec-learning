#!/usr/bin/env bash
# usercheck.sh - is this account present in the local account database?

ACCOUNT="$1"
grep "^$ACCOUNT:" /etc/passwd
RESULT=$?
echo "usercheck: grep exited with status $RESULT" >&2
exit "$RESULT"
