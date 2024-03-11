#!/usr/bin/python3
"""Functions for playing the prime game."""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(limit):
    """
    Generate prime numbers up to a given limit using
    the Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes


def can_make_move(nums, prime):
    """
    Check if a player can make a move by removing multiples of a prime number.

    Args:
        nums (list): List of remaining numbers in the game.
        prime (int): Prime number chosen by the player.

    Returns:
        bool: True if the player can make a move, False otherwise.
    """
    for num in nums:
        if num % prime == 0:
            return True
    return False


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the
        upper limit for each round.

    Returns:
        str: Name of the player who won the most rounds ('Maria' or 'Ben').
        If the winner cannot be determined, returns None.
    """
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        maria_turn = True

        while primes:
            if maria_turn:
                # Maria's turn
                prime = primes.pop(0)  # Choose the smallest prime
                if can_make_move(primes, prime):
                    primes = [num for num in primes if num % prime != 0]
                else:
                    wins["Ben"] += 1
                    break
            else:
                # Ben's turn
                if not any(can_make_move(primes, prime) for prime in primes):
                    wins["Maria"] += 1
                    break
            maria_turn = not maria_turn

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
