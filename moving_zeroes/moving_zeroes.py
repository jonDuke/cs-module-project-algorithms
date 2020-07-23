'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    end = len(arr)-1
    # find the last non-zero value
    while arr[end] == 0 and end > 0:
        end -= 1

    cur = 0
    # iterate through the array
    while cur < end:
        # if arr[cur] is 0, swap it with the end
        if arr[cur] == 0:
            arr[cur], arr[end] = arr[end], arr[cur]
            end -= 1
        cur += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")