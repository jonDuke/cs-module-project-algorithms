'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# runs in O(kn), takes ~38 seconds on the large input test
def sliding_window_max(nums, k):
    output = []
    # i is the first index of each valid window
    for i in range(len(nums)-k+1):
        # save the highest number in this window
        high = nums[i]
        for j in range(i,i+k):
            if nums[j] > high:
                high = nums[j]
        output.append(high)

    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
