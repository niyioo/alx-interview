#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    try:
        parts = line.split()
        if len(parts) >= 7:
            size = int(parts[-1])
            code = int(parts[-2])
            
            total_size += size

            if code in status_codes:
                status_codes[code] += 1

            return total_size, status_codes
    except ValueError:
        pass  # Ignore lines with invalid format or non-integer status code
    return total_size, status_codes