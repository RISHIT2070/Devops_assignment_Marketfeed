# Devops_assignment_Marketfeed

# Log Monitor

This Python script monitors a log file for lines containing specified keywords and prints a summary of the most frequent occurrences.

## Prerequisites

* Python 3.x

## Usage

1. Save the script as `log_monitor.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following arguments:

python log_monitor.py <log_file> <keyword1> [keyword2 ...]
- `<log_file>`: Path to the log file you want to monitor.
  - `<keyword1>`: First keyword to search for.
  - `[keyword2 ...]`: Optional additional keywords (space-separated).

## Example
python log_monitor.py server.log "ERROR" "WARNING"

This will monitor the `server.log` file for lines containing "ERROR" or "WARNING" and print the top 5 most frequent occurrences.

## Stopping the Script

Press `Ctrl+C` to stop the monitoring.
