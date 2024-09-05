#!/usr/bin/python3
"""Module defining isWinner function"""


def isWinner(x, nums):
    """ Function to see who has won the game"""
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Initialize scores and array of possible prime numbers
    ben_counter = 0
    maria_counter = 0
    # list 'sorted_list' of length sorted(nums)[-1] + 1 with all elements initialized to 1
    sorted_list = [1 for x in range(sorted(nums)[-1] + 1)]
    # The first two elements of the list, are set to 0
    # because 0 and 1 are not prime numbers
    sorted_list[0], sorted_list[1] = 0, 0
    # Sieve of Eratosthenes algorithm to generate array of prime numbers
    for j in range(2, len(sorted_list)):
        rm_multiples(sorted_list, j)
    # Play each round of the game
    for j in nums:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(sorted_list[0:j + 1]) % 2 == 0:
            ben_counter += 1
        else:
            maria_counter += 1
    # Determine the winner of the game
    if ben_counter > maria_counter:
        return "Ben"
    if maria_counter > ben_counter:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): An array of possible prime numbers.
        x (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """

    for j in range(2, len(ls)):
        try:
            ls[j * x] = 0
        except (ValueError, IndexError):
            break