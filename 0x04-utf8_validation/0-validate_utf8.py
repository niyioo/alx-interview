#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the bytes of the data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    remaining_bytes = 0

    for byte in data:
        leading_bit_mask = 1 << 7

        if not remaining_bytes:
            while byte & leading_bit_mask:
                remaining_bytes += 1
                leading_bit_mask >>= 1

            if not remaining_bytes:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
