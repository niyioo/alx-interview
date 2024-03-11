#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(limit):
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
    for num in nums:
        if num % prime == 0:
            return True
    return False


def isWinner(x, nums):
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
