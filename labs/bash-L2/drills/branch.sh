#!/usr/bin/env bash
STATUS="$1"
if [ "$STATUS" -eq 200 ]; then
    echo "ok"
elif [ "$STATUS" -eq 404 ]; then
    echo "not found"
elif [ "$STATUS" -eq 500 ]; then
    echo "server error"
else
    echo "unhandled status $STATUS"
fi
