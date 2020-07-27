'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# First pass solution was O(n log n) due to the sort() call

# def single_number(arr):
#     # sort arr so that all duplicate numbers will be next to each other
#     arr.sort()
#     for i in range(0, len(arr)-1, 2):
#         if arr[i] != arr[i+1]:
#             # didn't match, arr[i] is the single
#             return arr[i]
    
#     # loop will not get to the last value if it is the single
#     return arr[-1]

# second pass solution is O(n), specifically O(3n)
def single_number(arr):
    # initialize a counts dict
    counts = {}
    for n in arr:
        counts[n] = 0

    # count each values
    for n in arr:
        counts[n] += 1
    
    # return the item with count == 1
    for k in counts.keys():
        if counts[k] == 1:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
