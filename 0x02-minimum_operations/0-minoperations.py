#!/usr/bin/python3
"""
Module for minimum operations
"""


def minOperations(target):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters.
    """
    copied_chars = 1
    clipboard_count = 0
    operations_count = 0

    while copied_chars < target:
        if clipboard_count == 0:
            clipboard_count = copied_chars
            operations_count += 1

        if copied_chars == 1:
            copied_chars += clipboard_count
            operations_count += 1
            continue

        remaining_chars = target - copied_chars

        if remaining_chars < clipboard_count:
            return 0

        if remaining_chars % copied_chars != 0:
            copied_chars += clipboard_count
            operations_count += 1
        else:
            clipboard_count = copied_chars
            copied_chars += clipboard_count
            operations_count += 2

    if copied_chars == target:
        return operations_count
    else:
        return 0
