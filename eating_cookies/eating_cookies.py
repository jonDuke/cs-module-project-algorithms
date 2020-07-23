'''
Input: an integer
Returns: an integer
'''
#  Recursive brute force solution, times out on large tests
def eating_cookies(n, l=[]):
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        # 1+1 or 2
        return 2
    elif n == 3:
        # 1+1+1, 1+2, 2+1, 3
        return 4
    
    # Recursion: try each step and call again on the remainder
    # Since all smaller cases are returned above, n >= 4 here
    # Eat 1 then the rest
    sum = eating_cookies(n-1)
    # Eat 2 then the rest
    sum += eating_cookies(n-2)
    # Eat 3 then the rest
    sum += eating_cookies(n-3)

    return sum
            

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
