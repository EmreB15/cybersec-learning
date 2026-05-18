#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
F=auth-snippet.log
echo "=== total lines ==="
wc -l "$F"
echo "=== Failed count ==="
grep -c Failed "$F"
echo "=== Accepted count ==="
grep -c Accepted "$F"
echo "=== top IP filtered (CORRECT answer for retest) ==="
grep Failed "$F" | awk '{print $13}' | sort | uniq -c | sort -nr
echo "=== top IP unfiltered (TRAP answer if filter discipline fails) ==="
awk '{print $13}' "$F" | sort | uniq -c | sort -nr | head -7
echo "=== distinct invalid usernames in Failed (\$11) ==="
grep Failed "$F" | awk '{print $11}' | sort -u
echo "=== count of distinct usernames ==="
grep Failed "$F" | awk '{print $11}' | sort -u | wc -l
