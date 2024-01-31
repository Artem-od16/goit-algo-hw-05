import re
from typing import Dict, List


def parse_log_line(line: str) -> Dict:
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)")
    match = pattern.match(line)
    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3),
        }
    else:
        raise ValueError("Invalid log line format")


def load_logs(file_path: str) -> List[Dict]:
    with open(file_path, "r") as file:
        return [parse_log_line(line.strip()) for line in file]


def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: List[Dict]) -> Dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict):
    print("-" * 24)
    print("Logging Level    | Count")
    print("-----------------|------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")
