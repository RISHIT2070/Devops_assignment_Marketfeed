import time
import signal
import sys
import re

# Function to handle Ctrl+C
def signal_handler(sig, frame):
    print("\nStopping log monitoring...")
    sys.exit(0)

# Set up signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def read_log_file(log_file, keywords):
    try:
        with open(log_file, 'r') as file:
            while True:
                line = file.readline()
                if not line:  # Check for empty line
                    time.sleep(0.1)
                    continue  # Skip sleep on empty line
                for keyword in keywords:
                    if re.search(keyword, line):
                        yield line.strip()
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        print(f"Log file '{log_file}' not found.")
        sys.exit(1)


def count_occurrences(lines):
    counts = {}
    for line in lines:
        counts[line] = counts.get(line, 0) + 1
    return counts


def generate_summary(counts, top_n=5):
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print("Top error messages:")
    for i, (line, count) in enumerate(sorted_counts[:top_n], start=1):
        print(f"{i}. {line} - Count: {count}")


def main(log_file, keywords):
    print("Starting log monitoring...")
    lines = read_log_file(log_file, keywords)
    counts = count_occurrences(lines)
    generate_summary(counts)


if __name__ == "__main__":
    # Get log file and keywords from arguments
    if len(sys.argv) < 3:
        print("Usage: log_monitor.py <log_file> <keyword1> [keyword2 ...]")
        sys.exit(1)

    log_file = sys.argv[1]
    keywords = sys.argv[2:]
    main(log_file, keywords)
