def rotate_arr(nums: list, k: int) -> list:
    if not nums:
        return nums
    k = k % len(nums)
    if k == 0:
        return nums
    nums[:] = nums[-k:] + nums[:-k]
    return nums


arr = [1, 2, 3, 4, 5, 6]
rotate_arr(arr, 2)
print(arr)
