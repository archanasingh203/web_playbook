#!/bin/bash

# Parse a log file and extract lines with ERROR or WARNING
LOG_FILE=$1

if [[ ! -f "$LOG_FILE" ]]; then
  echo "Usage: $0 <log_file>"
  exit 1
fi

# Print all ERROR or WARNING lines
grep -E "ERROR|WARNING" "$LOG_FILE"

# Extract IP addresses from logs (assumes IPv4)
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$LOG_FILE" | sort | uniq

# Count occurrences of a specific error pattern
ERROR_PATTERN="Connection timed out"
COUNT=$(grep -c "$ERROR_PATTERN" "$LOG_FILE")
echo "Number of '$ERROR_PATTERN' errors: $COUNT"

# Find all usernames from login logs (user=someuser123)
grep -oE 'user=[a-zA-Z0-9_]+' "$LOG_FILE" | cut -d= -f2 | sort | uniq -c

# Extract date and time from logs like: [2025-04-28 17:45:12]
grep -oE '\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\]' "$LOG_FILE"

sleep 2


