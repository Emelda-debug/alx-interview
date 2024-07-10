#!/usr/bin/python3
""" method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
   method to calculate the fewest number of operations needed
   to result in exactly n H characters in the file.
    Arguments:
        n: input value
        save_list: List to save all the operations
    Return: sum of the operations
    """
    if n < 2:
        return 0
    save_list = []
    x = 1
    while n != 1:
        x += 1
        if n % x == 0:
            while n % x == 0:
                n /= x
                save_list.append(x)
    return sum(save_list)
