#!/usr/bin/python3
"""
Module for making change with coins
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    amount_so_far = 0
    coins_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        num_coins = (total - amount_so_far) // coin
        amount_so_far += num_coins * coin
        coins_used += num_coins
        if amount_so_far == total:
            return coins_used
    return -1
