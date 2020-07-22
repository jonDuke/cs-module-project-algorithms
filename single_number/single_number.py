'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # sort arr so that all duplicate numbers will be next to each other
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        if arr[i] != arr[i+1]:
            # didn't match, arr[i] is the single
            return arr[i]
    
    # loop will not get to the last value if it is the single
    return arr[-1]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
