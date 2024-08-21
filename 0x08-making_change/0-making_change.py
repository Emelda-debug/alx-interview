#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins: list, total: int) -> int:
    """ Function to determine the fewest number
    of coins needed to meet a given amount total

    Args:
        coins ([List]): list of Coins available
        total ([int]): total amount needed
    """
    if total <= 0:
        return 0
    counter = 0
    num_of_coins = 0
    coins.sort(reverse=True)
    for x in coins:
        while counter < total:
            counter += x
            num_of_coins += 1
        if counter == total:
            return num_of_coins
        counter -= x
        num_of_coins -= 1
    return -1
