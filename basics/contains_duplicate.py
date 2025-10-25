class Solution:
    def containsDuplicate(self, nums) -> bool:
        # Use a set for faster lookup and start with an empty set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example usage:
nums = [1,2,3,1]

print(Solution().containsDuplicate(nums))  # Output: True

# Explanation:
# The original code used 'range(1, len(nums)-1)', which skips the last element.
# For nums = [1,2,3,1], the last '1' was not checked, so it returned False.
# The fixed code checks all elements, so it correctly returns True.