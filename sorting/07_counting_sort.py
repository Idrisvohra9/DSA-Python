"""
COUNTING SORT
=============
Time Complexity: O(n + k) where k is the range of input
Space Complexity: O(k)
Stable: Yes (maintains relative order of equal elements)

How it works:
- Count frequency of each element
- Calculate cumulative sum to determine positions
- Place elements in their correct positions based on counts
- Works well when range of elements (k) is small compared to number of elements (n)
- Not comparison-based sorting algorithm

Note: Works only with non-negative integers or can be adapted for other ranges
"""

def counting_sort(arr):
    """
    Sorts an array using counting sort algorithm.
    Assumes all elements are non-negative integers.
    
    Args:
        arr: List of non-negative integers
    Returns:
        Sorted list in ascending order
    """
    # Handle empty array
    if not arr:
        return arr
    
    # Find the maximum element to determine range
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Create count array to store frequency of each element
    # Initialize all counts as 0
    count = [0] * range_val
    
    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Build the sorted array
    sorted_arr = []
    for i in range(range_val):
        # Add each element count[i] times to result
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr


def counting_sort_stable(arr):
    """
    Stable version of counting sort that maintains relative order.
    Uses cumulative sum approach.
    
    Args:
        arr: List of non-negative integers
    Returns:
        Sorted list maintaining stability
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Count frequency of each element
    count = [0] * range_val
    for num in arr:
        count[num - min_val] += 1
    
    # Calculate cumulative sum
    # count[i] now contains actual position of element i in sorted array
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Build the result array
    result = [0] * len(arr)
    
    # Build output array from right to left to maintain stability
    for i in range(len(arr) - 1, -1, -1):
        element = arr[i]
        result[count[element - min_val] - 1] = element
        count[element - min_val] -= 1
    
    return result


def counting_sort_in_place(arr):
    """
    In-place version of counting sort (modifies original array).
    
    Args:
        arr: List to sort in place
    """
    if not arr:
        return
    
    sorted_arr = counting_sort(arr)
    
    # Copy sorted elements back to original array
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]


def counting_sort_with_steps(arr):
    """
    Counting sort with step-by-step visualization.
    Shows the counting and placement process.
    """
    print(f"Original array: {arr}")
    
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    print(f"Range: {min_val} to {max_val} (total range: {range_val})")
    
    # Step 1: Count frequencies
    count = [0] * range_val
    print(f"\nStep 1: Counting frequencies")
    print(f"Initial count array: {count}")
    
    for num in arr:
        count[num - min_val] += 1
        print(f"  Processing {num}: count[{num - min_val}] = {count[num - min_val]}")
    
    print(f"Final count array: {count}")
    
    # Step 2: Build sorted array
    print(f"\nStep 2: Building sorted array")
    sorted_arr = []
    for i in range(range_val):
        element = i + min_val
        frequency = count[i]
        if frequency > 0:
            print(f"  Adding {element} × {frequency} times")
            sorted_arr.extend([element] * frequency)
    
    print(f"Final sorted array: {sorted_arr}")
    return sorted_arr


def counting_sort_for_strings(arr):
    """
    Counting sort adapted for sorting strings by their first character.
    
    Args:
        arr: List of strings
    Returns:
        List sorted by first character of each string
    """
    if not arr:
        return arr
    
    # Assuming ASCII characters (0-127)
    count = [0] * 128
    
    # Count frequency of first character of each string
    for string in arr:
        if string:  # Check if string is not empty
            count[ord(string[0])] += 1
    
    # Build sorted array
    result = []
    for i in range(128):
        if count[i] > 0:
            # Find all strings that start with character chr(i)
            for string in arr:
                if string and ord(string[0]) == i:
                    result.append(string)
    
    return result


def counting_sort_negative_numbers(arr):
    """
    Counting sort adapted to handle negative numbers.
    
    Args:
        arr: List of integers (can include negative numbers)
    Returns:
        Sorted list
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Shift all values to make them non-negative
    count = [0] * range_val
    
    for num in arr:
        count[num - min_val] += 1
    
    # Build sorted array
    sorted_arr = []
    for i in range(range_val):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr


# Test the counting sort functions
if __name__ == "__main__":
    # Test 1: Basic counting sort
    test_arr1 = [4, 2, 2, 8, 3, 3, 1]
    print("=== BASIC COUNTING SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", counting_sort(test_arr1))
    
    # Test 2: Stable counting sort
    test_arr2 = [1, 4, 1, 2, 7, 5, 2]
    print("\n=== STABLE COUNTING SORT ===")
    print("Original array:", test_arr2)
    print("Sorted array:", counting_sort_stable(test_arr2))
    
    # Test 3: Array with larger range
    test_arr3 = [10, 5, 0, 3, 8, 6, 2, 7, 1, 4]
    print("\n=== LARGER RANGE ===")
    print("Original array:", test_arr3)
    print("Sorted array:", counting_sort(test_arr3))
    
    # Test 4: Array with duplicates
    test_arr4 = [3, 3, 3, 1, 1, 2, 2, 2, 2]
    print("\n=== WITH DUPLICATES ===")
    print("Original array:", test_arr4)
    print("Sorted array:", counting_sort(test_arr4))
    
    # Test 5: Negative numbers
    test_arr5 = [-5, -2, -8, -1, -3]
    print("\n=== WITH NEGATIVE NUMBERS ===")
    print("Original array:", test_arr5)
    print("Sorted array:", counting_sort_negative_numbers(test_arr5))
    
    # Test 6: String sorting by first character
    test_strings = ["banana", "apple", "cherry", "date", "berry"]
    print("\n=== SORTING STRINGS BY FIRST CHARACTER ===")
    print("Original array:", test_strings)
    print("Sorted array:", counting_sort_for_strings(test_strings))
    
    # Test 7: Step-by-step demonstration
    test_arr7 = [4, 2, 2, 8, 3, 3, 1]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    counting_sort_with_steps(test_arr7)
    
    # Test 8: Edge cases
    print("\n=== EDGE CASES ===")
    print("Empty array:", counting_sort([]))
    print("Single element:", counting_sort([5]))
    print("Already sorted:", counting_sort([1, 2, 3, 4, 5]))