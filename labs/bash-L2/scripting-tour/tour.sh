#!/usr/bin/env bash
# tour.sh - a teaching tour of five constructs. This is NOT your task.

echo "[1] a variable: assign with =, read back with \$NAME"
COLOUR="blue"
echo "    COLOUR holds: $COLOUR"

echo "[2] \$1 is the first argument this script was called with"
echo "    I was called with: $1"

echo "[3] an argument can go straight into a variable"
TARGET="$1"
echo "    TARGET holds: $TARGET"

echo "[4] run a command, then read its exit code from \$?"
ls "$TARGET"
CODE=$?
echo "    ls exited with code: $CODE"

echo "[5] two output streams, same script"
echo "    this is DATA -> stdout"
echo "    this is COMMENTARY -> stderr" >&2

echo "[6] exit with a code I choose"
exit "$CODE"
