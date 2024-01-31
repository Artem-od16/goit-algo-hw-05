import sys

from functions import (
    count_logs_by_level,
    display_log_counts,
    filter_logs_by_level,
    load_logs,
)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python3 task3/main.py task3/file.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, log_level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        # Display detailed logs for the specified level
        if log_level in counts:
            print(f"\nDetails for log level '{log_level}':")
            for log in filtered_logs:
                print(f"{log['timestamp']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()
