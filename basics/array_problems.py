"""
ARRAY PROBLEMS & SOLUTIONS
==========================
Collection of well-known array problems with optimal solutions.
Arrays are fundamental data structures with contiguous memory allocation,
providing O(1) access time and efficient cache performance.
"""

# ============================================================================
# PROBLEM 1: TWO SUM
# ============================================================================
def two_sum(nums, target):
    """
    Problem: Find two numbers in array that add up to target.
    
    Approach: Hash map for O(n) solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: nums=[2,7,11,15], target=9 → [0,1] (2+7=9)
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []

def two_sum_sorted(nums, target):
    """
    Two Sum variant for sorted array using two pointers.
    Time Complexity: O(n), Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# ============================================================================
# PROBLEM 2: BEST TIME TO BUY AND SELL STOCK
# ============================================================================
def max_profit(prices):
    """
    Problem: Find maximum profit from buying and selling stock once.
    
    Approach: Track minimum price and maximum profit
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [7,1,5,3,6,4] → 5 (buy at 1, sell at 6)
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Update maximum profit if selling today
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

def max_profit_multiple_transactions(prices):
    """
    Variant: Multiple transactions allowed.
    Buy low, sell high strategy.
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

# ============================================================================
# PROBLEM 3: CONTAINS DUPLICATE
# ============================================================================
def contains_duplicate(nums):
    """
    Problem: Check if array contains any duplicates.
    
    Approach: Hash set for O(n) detection
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def contains_nearby_duplicate(nums, k):
    """
    Variant: Check if duplicates are within k distance.
    """
    num_indices = {}
    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    return False

# ============================================================================
# PROBLEM 4: MAXIMUM SUBARRAY (KADANE'S ALGORITHM)
# ============================================================================
def max_subarray(nums):
    """
    Problem: Find contiguous subarray with maximum sum.
    
    Approach: Kadane's Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 ([4,-1,2,1])
    """
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend current subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_with_indices(nums):
    """
    Variant: Return the actual subarray indices.
    """
    max_sum = nums[0]
    current_sum = nums[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return nums[start:end+1], max_sum

# ============================================================================
# PROBLEM 5: PRODUCT OF ARRAY EXCEPT SELF
# ============================================================================
def product_except_self(nums):
    """
    Problem: Return array where each element is product of all others.
    Cannot use division operator.
    
    Approach: Left and right products
    Time Complexity: O(n)
    Space Complexity: O(1) excluding output array
    
    Example: [1,2,3,4] → [24,12,8,6]
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Calculate right products and multiply
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# ============================================================================
# PROBLEM 6: MAXIMUM PRODUCT SUBARRAY
# ============================================================================
def max_product(nums):
    """
    Problem: Find contiguous subarray with maximum product.
    
    Approach: Track both max and min products (negatives can become max)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [2,3,-2,4] → 6 ([2,3])
    """
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        # If current number is negative, swap max and min
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update max and min products
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        # Update result
        result = max(result, max_product)
    
    return result

# ============================================================================
# PROBLEM 7: FIND MINIMUM IN ROTATED SORTED ARRAY
# ============================================================================
def find_min(nums):
    """
    Problem: Find minimum element in rotated sorted array.
    
    Approach: Modified binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Example: [3,4,5,1,2] → 1
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return nums[left]

def search_rotated_array(nums, target):
    """
    Variant: Search for target in rotated sorted array.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# ============================================================================
# PROBLEM 8: 3SUM
# ============================================================================
def three_sum(nums):
    """
    Problem: Find all unique triplets that sum to zero.
    
    Approach: Sort + two pointers
    Time Complexity: O(n²)
    Space Complexity: O(1) excluding output
    
    Example: [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

# ============================================================================
# PROBLEM 9: CONTAINER WITH MOST WATER
# ============================================================================
def max_area(height):
    """
    Problem: Find two lines that form container with most water.
    
    Approach: Two pointers from ends
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [1,8,6,2,5,4,8,3,7] → 49
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_area = width * min(height[left], height[right])
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# ============================================================================
# PROBLEM 10: MERGE INTERVALS
# ============================================================================
def merge_intervals(intervals):
    """
    Problem: Merge overlapping intervals.
    
    Approach: Sort by start time, then merge
    Time Complexity: O(n log n)
    Space Complexity: O(1) excluding output
    
    Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            # Overlapping intervals, merge them
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Non-overlapping interval, add to result
            merged.append(current)
    
    return merged

# ============================================================================
# PROBLEM 11: SLIDING WINDOW MAXIMUM
# ============================================================================
from collections import deque

def max_sliding_window(nums, k):
    """
    Problem: Find maximum in each sliding window of size k.
    
    Approach: Monotonic decreasing deque
    Time Complexity: O(n)
    Space Complexity: O(k)
    
    Example: nums=[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]
    """
    if not nums or k == 0:
        return []
    
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices of smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# ============================================================================
# PROBLEM 12: TRAPPING RAIN WATER
# ============================================================================
def trap(height):
    """
    Problem: Calculate trapped rainwater after raining.
    
    Approach: Two pointers with max heights
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [0,1,0,2,1,0,1,3,2,1,2,1] → 6
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water

# ============================================================================
# PROBLEM 13: LONGEST INCREASING SUBSEQUENCE
# ============================================================================
def length_of_lis(nums):
    """
    Problem: Find length of longest increasing subsequence.
    
    Approach: Dynamic programming with binary search optimization
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Example: [10,9,2,5,3,7,101,18] → 4 ([2,3,7,101])
    """
    if not nums:
        return 0
    
    # tails[i] = smallest ending element of increasing subsequence of length i+1
    tails = []
    
    for num in nums:
        # Binary search for position to insert/replace
        left, right = 0, len(tails)
        
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements, append
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)

# ============================================================================
# PROBLEM 14: SUBARRAY SUM EQUALS K
# ============================================================================
def subarray_sum(nums, k):
    """
    Problem: Count number of subarrays with sum equal to k.
    
    Approach: Prefix sum with hash map
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: nums=[1,1,1], k=2 → 2
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum -> frequency
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Update frequency of current prefix sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count

# ============================================================================
# PROBLEM 15: MEETING ROOMS II
# ============================================================================
import heapq

def min_meeting_rooms(intervals):
    """
    Problem: Find minimum number of meeting rooms needed.
    
    Approach: Sort by start time, use min heap for end times
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Example: [[0,30],[5,10],[15,20]] → 2
    """
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times of ongoing meetings
    min_heap = []
    
    for start, end in intervals:
        # Remove meetings that have ended
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        
        # Add current meeting's end time
        heapq.heappush(min_heap, end)
    
    return len(min_heap)

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def test_array_problems():
    """Test all array problems with examples."""
    
    print("=== ARRAY PROBLEMS & SOLUTIONS ===\n")
    
    # Test 1: Two Sum
    print("1. TWO SUM")
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Array: {nums1}, Target: {target1}")
    print(f"Indices: {two_sum(nums1, target1)}")
    
    # Test 2: Best Time to Buy and Sell Stock
    print("\n2. BEST TIME TO BUY AND SELL STOCK")
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices}")
    print(f"Max profit (one transaction): {max_profit(prices)}")
    print(f"Max profit (multiple transactions): {max_profit_multiple_transactions(prices)}")
    
    # Test 3: Contains Duplicate
    print("\n3. CONTAINS DUPLICATE")
    test_arrays = [[1, 2, 3, 1], [1, 2, 3, 4]]
    for arr in test_arrays:
        print(f"Array: {arr} → Has duplicate: {contains_duplicate(arr)}")
    
    # Test 4: Maximum Subarray
    print("\n4. MAXIMUM SUBARRAY (KADANE'S ALGORITHM)")
    nums4 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {nums4}")
    print(f"Max sum: {max_subarray(nums4)}")
    subarray, max_sum = max_subarray_with_indices(nums4)
    print(f"Max subarray: {subarray} with sum: {max_sum}")
    
    # Test 5: Product of Array Except Self
    print("\n5. PRODUCT OF ARRAY EXCEPT SELF")
    nums5 = [1, 2, 3, 4]
    print(f"Input: {nums5}")
    print(f"Output: {product_except_self(nums5)}")
    
    # Test 6: Maximum Product Subarray
    print("\n6. MAXIMUM PRODUCT SUBARRAY")
    nums6 = [2, 3, -2, 4]
    print(f"Array: {nums6}")
    print(f"Max product: {max_product(nums6)}")
    
    # Test 7: Find Minimum in Rotated Sorted Array
    print("\n7. FIND MINIMUM IN ROTATED SORTED ARRAY")
    rotated = [3, 4, 5, 1, 2]
    print(f"Rotated array: {rotated}")
    print(f"Minimum: {find_min(rotated)}")
    print(f"Search 4: index {search_rotated_array(rotated, 4)}")
    
    # Test 8: 3Sum
    print("\n8. THREE SUM")
    nums8 = [-1, 0, 1, 2, -1, -4]
    print(f"Array: {nums8}")
    print(f"Triplets summing to 0: {three_sum(nums8)}")
    
    # Test 9: Container With Most Water
    print("\n9. CONTAINER WITH MOST WATER")
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Heights: {heights}")
    print(f"Max area: {max_area(heights)}")
    
    # Test 10: Merge Intervals
    print("\n10. MERGE INTERVALS")
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Intervals: {intervals}")
    print(f"Merged: {merge_intervals(intervals)}")
    
    # Test 11: Trapping Rain Water
    print("\n11. TRAPPING RAIN WATER")
    heights11 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Heights: {heights11}")
    print(f"Trapped water: {trap(heights11)}")
    
    # Test 12: Longest Increasing Subsequence
    print("\n12. LONGEST INCREASING SUBSEQUENCE")
    nums12 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Array: {nums12}")
    print(f"LIS length: {length_of_lis(nums12)}")
    
    # Test 13: Subarray Sum Equals K
    print("\n13. SUBARRAY SUM EQUALS K")
    nums13 = [1, 1, 1]
    k13 = 2
    print(f"Array: {nums13}, k: {k13}")
    print(f"Count of subarrays: {subarray_sum(nums13, k13)}")

if __name__ == "__main__":
    test_array_problems()