class Solution:
    def findMedianSortedArrays(self, nums1=[], nums2=[]) -> float:
        merged_arr = nums1 + nums2
        merged_arr.sort()
        n = len(merged_arr)
        if n % 2 == 1:
            # If the length of the merged array is odd, return the middle element
            return merged_arr[n // 2]
        else:
            # If the length of the merged array is even, return the average of the two middle elements
            mid1 = n // 2 - 1
            mid2 = n // 2
            return (merged_arr[mid1] + merged_arr[mid2]) / 2


# Example usage:
nums1 = [1, 3, 5, 7, 9]
nums2 = [2]
# nums1.extend(nums2)
# print(nums1 + nums2)
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.0
