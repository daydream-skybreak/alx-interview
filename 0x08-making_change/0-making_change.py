#!/usr/bin/python3
"""module that makes change with the least count to total"""


def makeChange(coins, total):
    """method that makes change for total
    """
    sorted_coins = sorted(coins, reverse=True)
    coin_count = 0
    idx = 0
    length = len(coins)
    while total > 0:
        if idx >= length:
            return -1
        if total >= sorted_coins[idx]:
            total -= sorted_coins[idx]
            coin_count += 1
        else:
            idx += 1
    return coin_count
