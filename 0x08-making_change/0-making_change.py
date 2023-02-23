#!/usr/bin/python3
"""
interview ALX: Making change
SE: Diabakate Ikary
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1
        - Coins is a list of the values of the coins in your possession
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination of
        coin in the list
    """
    sum = 0
    if (total <= 0):
        return 0
    coins.sort(reverse=True)
    for n in coins:
        if (total < n):
            pass
        q, r = divmod(total, n)
        total = r
        sum += q
    if (total != 0):
        return -1
    return sum
