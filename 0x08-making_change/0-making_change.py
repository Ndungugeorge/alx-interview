#!/usr/bin/python3
"""
dynamic programming
"""


def makeChange(coins, total):
    """
    Given a pile of cons of different values,
    determine the fewest number of cons needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
