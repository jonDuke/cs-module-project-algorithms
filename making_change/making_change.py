#!/usr/bin/python

import sys

# This solution works by finding all possible permutations of coins, then
# removing duplicates.  It is horribly inefficient, but it works.
# (hangs on amount=100)
def making_change(amount, denominations):
    print("finding solutions for amount", amount)
    # Call the recursive function to find all possible solutions
    all_solutions = []
    find_solutions(amount, denominations, all_solutions)

    # Return the number of solutions found
    return len(all_solutions)

def find_solutions(amount, denominations, all_solutions, solution=[]):
    # Base case: can only use smallest coin
    if amount <= denominations[0]:
        # add the remaining coins to the solution
        for _ in range(amount//denominations[0]):
            solution.append(denominations[0])
        # sort for comparison
        solution.sort()
        # add solution if it has not already been found
        if solution not in all_solutions:
            all_solutions.append(solution)
        return
    
    # Recursion: add 1 of each coin, calculate possibilities for the remainder
    for coin in denominations:
        if amount >= coin:
            # Add one of that coin, then re-call on remainder
            new_sol = solution.copy()
            new_sol.append(coin)
            find_solutions(amount-coin, denominations, all_solutions, new_sol)

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
