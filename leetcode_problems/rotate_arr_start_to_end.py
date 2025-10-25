"""
Rotate an Array by d - Counterclockwise or Left
Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

Input: arr[] = {1, 2, 3}, d = 4
Output: {2, 3, 1}
Explanation: The array is rotated as follows:

After first left rotation, arr[] = {2, 3, 1}
After second left rotation, arr[] = {3, 1, 2}
After third left rotation, arr[] = {1, 2, 3}
After fourth left rotation, arr[] = {2, 3, 1}

"""

# Swapping method
# def rotate_arr(arr: list, d: int) -> list:
#     n = len(arr)


#     for i in range(d):
#         first = arr[0]
#         for j in range(n - 1):
#             arr[j] = arr[j + 1]
#         arr[n - 1] = first

# Splitting method:


def rotate_arr(nums: list, k: int) -> list:
    # handle empty list to avoid ZeroDivisionError
    n = len(nums)
    if n == 0:
        return

    # normalize k so it is within the array length (handles k >= n)
    k = k % n

    # if k is 0 after normalization, no rotation is needed
    if k == 0:
        return

    # For a left rotation by k positions:
    # - the elements from index k to end become the new prefix: nums[k:]
    # - the first k elements move to the end: nums[:k]
    # Combine them and assign back to the original list using slice assignment
    # so the list object is modified in-place.
    nums[:] = nums[k:] + nums[:k]

    # function modifies nums in-place and returns None
    return


arr = [1, 2, 3, 4, 5, 6]
rotate_arr(arr, 2)
print(arr)
