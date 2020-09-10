def linear_search(arr, target):
    for ii, num in enumerate(arr):
        if num == target:
            return ii

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = low + high //2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found
