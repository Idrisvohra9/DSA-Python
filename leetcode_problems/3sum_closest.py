from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closestSum - target):
                    closestSum = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return int(closestSum)


print(Solution().threeSumClosest([10, 20, 30, 40, 50, 60, 70, 80, 90], 1))
