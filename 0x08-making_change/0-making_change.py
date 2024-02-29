#!/usr/bin/python3
"""
Module for making change with coins
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    """
    if total < 0:
        return -1

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Zero coins are needed to make a total of 0

    # Iterate over each coin denomination
    for coin in coins:
        # Update min_coins[j] if it can be reduced by using the current coin
        for j in range(coin, total + 1):
            min_coins[j] = min(min_coins[j], min_coins[j - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
