#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the bytes of the data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    # Iterate through the data bytes
    i = 0
    while i < len(data):
        # Count the number of set high bits in the starting byte
        high_bits = bin(data[i])[2:].zfill(8).index('0')

        # Check if the number of following bytes matches the expected count
        if high_bits == 1 or high_bits > 4 or i + high_bits - 1 >= len(data):
            return False

        # Check that the following bytes all start with '10'
        for j in range(1, high_bits):
            if not (data[i + j] >> 6 == 0b10):
                return False

        # Move the index to the next character
        i += high_bits

    return True
