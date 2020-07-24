#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # Initialize cache
    cache = [0] * (amount + 1)
    cache[0] = 1

    # For each possible coin, starting with the smallest
    for coin in denominations:
        # For every amount between that coin value and the total amount
        for amount2 in range(coin, amount + 1):
            # Add the number of solutions found if we took out that coin
            cache[amount2] += cache[amount2 - coin]

    return cache[amount]

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
    else:
        print("Usage: making_change.py [amount]")
