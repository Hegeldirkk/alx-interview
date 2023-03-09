#!/usr/bin/python3
"""
SE: Ikary Diabakate
Prime Game
"""


def is_prime(n):
    """ Checks if a number given n is a prime number """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def calculate_pr(n, primes):
    """ Calculate all primes """
    top = primes[-1]
    if n > top:
        for i in range(top + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    """

    players_wins = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_pr(max(nums), primes)

    for round in range(x):
        sum_op = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])

        if (sum_op % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
