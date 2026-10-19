#!/usr/bin/env bash
ls /nope/nothing 2>/dev/null
echo "about to read the code"
CODE=$?
echo "CODE is $CODE   <-- captured AFTER an echo ran"

ls /nope/nothing 2>/dev/null
CODE=$?
echo "CODE is $CODE   <-- captured on the very next line"
