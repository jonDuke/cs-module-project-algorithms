'''
Input: an integer
Returns: an integer
'''
#  Recursive brute force solution, times out on large tests
def eating_cookies(n, cache=None):
    # Base cases: n == 1 or lower
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif cache is not None and cache[n] > 0:
        # we've already found this answer, just return it
        return cache[n]
    else:
        if cache is None:
            # initialize the cache
            cache = [0 for i in range(n+1)]
        
        # find recursive anser, store it in cache
        cache[n] = (eating_cookies(n-1, cache) +
                    eating_cookies(n-2, cache) +
                    eating_cookies(n-3, cache))
    
    return cache[n]
            

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
