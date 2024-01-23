#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


status_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_list = line.split()

        if "GET" in line and "HTTP/1.1" in line:
            status_code = line_list[-2]
            size = int(line_list[-1])

            if status_code in status_count:
                status_count[status_code] += 1
            total_size += size
            line_counter += 1

        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_count.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_count.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
