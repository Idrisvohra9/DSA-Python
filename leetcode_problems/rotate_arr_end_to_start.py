def rotate_arr(nums: list, k: int) -> list:
    k = k % len(nums)
    if k == 0:
        return
    nums[:k], nums[k:] = nums[-k:], nums[:-k]
    return


arr = [1, 2, 3, 4, 5, 6]
rotate_arr(arr, 2)
print(arr)
