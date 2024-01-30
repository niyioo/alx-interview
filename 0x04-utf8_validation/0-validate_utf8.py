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
    # Helper function to check if the given byte is a valid starting byte
    def is_starting_byte(byte):
        return (byte >> 6) != 0b10

    following_bytes = [0, 1, 1, 1, 1, 2, 2, 3, 3]

    # Iterate through the data bytes
    i = 0
    while i < len(data):
        # Count the number of set high bits in the starting byte
        high_bits = bin(data[i] >> 3)[2:].count('1')

        # Check if the number of following bytes matches the expected count
        if high_bits > 0:
            if high_bits > 4 or i + following_bytes[high_bits] > len(data):
                return False

            # Check that the following bytes all start with '10'
            for j in range(1, following_bytes[high_bits]):
                if not (data[i + j] >> 6 == 0b10):
                    return False

            # Move the index to the next character
            i += following_bytes[high_bits]
        else:
            i += 1

    return True
