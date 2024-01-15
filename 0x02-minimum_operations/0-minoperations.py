#!/usr/bin/python3
"""
Module for minimum operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.
    """
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations for each number of characters
    min_ops = [float('inf')] * (n + 1)

    # Base case: 1 H character requires 0 operations
    min_ops[1] = 0

    # Loop through each number of characters
    for i in range(2, n + 1):
        # Check if i is prime
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                # i is not prime, calculate minimum operations
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n]
