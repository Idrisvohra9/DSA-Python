"""
BINARY SEARCH
=============
An efficient searching algorithm that works on SORTED arrays.
It repeatedly divides the search space in half by comparing the target with the middle element.

Key Requirements:
- Array MUST be sorted
- Uses divide-and-conquer approach

How it works:
1. Find the middle element of the array
2. If middle element equals target, we found it!
3. If target is smaller than middle, search the left half
4. If target is larger than middle, search the right half
5. Repeat until found or no more elements to check

Time Complexity: O(log n) - much faster than linear search for large arrays
Space Complexity: O(1) for iterative version, O(log n) for recursive version
"""

def binary_search(arr, target):
    """
    Search for target in sorted array using binary search (iterative version).
    
    Args:
        arr: SORTED list of elements
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    # Set boundaries for our search area
    left = 0                    # Start of search area
    right = len(arr) - 1        # End of search area
    
    # Keep searching while there are elements to check
    while left <= right:
        # Find middle point (avoid overflow by using this formula)
        middle = left + (right - left) // 2
        
        # Check if we found our target
        if arr[middle] == target:
            return middle  # Found it! Return the index
        
        # If target is smaller, it must be in the left half
        elif arr[middle] > target:
            right = middle - 1  # Eliminate right half
        
        # If target is larger, it must be in the right half
        else:
            left = middle + 1   # Eliminate left half
    
    # Target not found
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary search using recursion (calls itself).
    
    Args:
        arr: SORTED list of elements
        target: Element we're looking for
        left: Starting index of current search area
        right: Ending index of current search area
    
    Returns:
        Index of target if found, -1 if not found
    """
    # Set right boundary if not provided
    if right is None:
        right = len(arr) - 1
    
    # Base case: no more elements to search
    if left > right:
        return -1
    
    # Find middle element
    middle = left + (right - left) // 2
    
    # Found the target!
    if arr[middle] == target:
        return middle
    
    # Target is in left half
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, left, middle - 1)
    
    # Target is in right half
    else:
        return binary_search_recursive(arr, target, middle + 1, right)


def binary_search_with_steps(arr, target):
    """
    Binary search with step-by-step explanation.
    Shows how the search space gets divided.
    """
    print(f"Searching for {target} in sorted array: {arr}")
    
    left = 0
    right = len(arr) - 1
    step = 1
    
    while left <= right:
        middle = left + (right - left) // 2
        middle_value = arr[middle]
        
        print(f"\nStep {step}:")
        print(f"  Search area: indices {left} to {right}")
        print(f"  Search area values: {arr[left:right+1]}")
        print(f"  Middle index: {middle}, Middle value: {middle_value}")
        
        if middle_value == target:
            print(f"  ✅ Found {target} at index {middle}!")
            return middle
        
        elif middle_value > target:
            print(f"  {middle_value} > {target}, search LEFT half")
            right = middle - 1
        
        else:
            print(f"  {middle_value} < {target}, search RIGHT half")
            left = middle + 1
        
        step += 1
    
    print(f"  ❌ {target} not found in array")
    return -1


def binary_search_first_occurrence(arr, target):
    """
    Find the FIRST occurrence of target in a sorted array with duplicates.
    
    Args:
        arr: SORTED array that may contain duplicates
        target: Element to find first occurrence of
    
    Returns:
        Index of first occurrence, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    result = -1  # Store the first occurrence found so far
    
    while left <= right:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            result = middle        # This might be the first occurrence
            right = middle - 1     # Continue searching in left half for earlier occurrence
        
        elif arr[middle] > target:
            right = middle - 1
        
        else:
            left = middle + 1
    
    return result


def binary_search_last_occurrence(arr, target):
    """
    Find the LAST occurrence of target in a sorted array with duplicates.
    
    Args:
        arr: SORTED array that may contain duplicates
        target: Element to find last occurrence of
    
    Returns:
        Index of last occurrence, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    result = -1  # Store the last occurrence found so far
    
    while left <= right:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            result = middle        # This might be the last occurrence
            left = middle + 1      # Continue searching in right half for later occurrence
        
        elif arr[middle] > target:
            right = middle - 1
        
        else:
            left = middle + 1
    
    return result


def binary_search_range(arr, target):
    """
    Find the range (first and last positions) of target in sorted array.
    
    Args:
        arr: SORTED array
        target: Element to find range for
    
    Returns:
        Tuple of (first_index, last_index), or (-1, -1) if not found
    """
    first = binary_search_first_occurrence(arr, target)
    
    if first == -1:
        return (-1, -1)  # Target not found
    
    last = binary_search_last_occurrence(arr, target)
    return (first, last)


def binary_search_insertion_point(arr, target):
    """
    Find the position where target should be inserted to keep array sorted.
    This is useful for insertion operations.
    
    Args:
        arr: SORTED array
        target: Element to find insertion point for
    
    Returns:
        Index where target should be inserted
    """
    left = 0
    right = len(arr)  # Note: right is len(arr), not len(arr)-1
    
    while left < right:
        middle = left + (right - left) // 2
        
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle
    
    return left


def binary_search_in_rotated_array(arr, target):
    """
    Binary search in a rotated sorted array.
    A rotated array is like [4,5,6,7,0,1,2] (originally [0,1,2,4,5,6,7]).
    
    Args:
        arr: Rotated sorted array (no duplicates)
        target: Element to search for
    
    Returns:
        Index of target if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            return middle
        
        # Check which half is properly sorted
        if arr[left] <= arr[middle]:  # Left half is sorted
            # Check if target is in the sorted left half
            if arr[left] <= target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        else:  # Right half is sorted
            # Check if target is in the sorted right half
            if arr[middle] < target <= arr[right]:
                left = middle + 1
            else:
                right = middle - 1
    
    return -1


def binary_search_peak_element(arr):
    """
    Find a peak element in array (element that is greater than its neighbors).
    Array is not necessarily sorted for this problem.
    
    Args:
        arr: Array of numbers
    
    Returns:
        Index of a peak element
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        middle = left + (right - left) // 2
        
        # If middle element is smaller than next element,
        # peak must be in the right half
        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            # Peak is in left half (including middle)
            right = middle
    
    return left


def binary_search_sqrt(number):
    """
    Find square root of a number using binary search.
    Returns the largest integer whose square is ≤ number.
    
    Args:
        number: Non-negative integer
    
    Returns:
        Integer square root
    """
    if number < 2:
        return number
    
    left = 1
    right = number // 2
    result = 0
    
    while left <= right:
        middle = left + (right - left) // 2
        square = middle * middle
        
        if square == number:
            return middle
        elif square < number:
            result = middle    # This might be our answer
            left = middle + 1
        else:
            right = middle - 1
    
    return result


# Test all binary search functions
if __name__ == "__main__":
    print("=== BINARY SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic binary search
    print("1. BASIC BINARY SEARCH")
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    result = binary_search(sorted_array, target)
    print(f"Array: {sorted_array}")
    print(f"Searching for: {target}")
    print(f"Found at index: {result}")
    
    # Test 2: Binary search with steps
    print("\n2. BINARY SEARCH WITH STEPS")
    binary_search_with_steps([1, 3, 5, 7, 9, 11, 13], 5)
    
    # Test 3: Recursive binary search
    print("\n3. RECURSIVE BINARY SEARCH")
    result_recursive = binary_search_recursive([2, 4, 6, 8, 10, 12], 8)
    print(f"Recursive search result: {result_recursive}")
    
    # Test 4: Search for non-existent element
    print("\n4. SEARCH FOR NON-EXISTENT ELEMENT")
    binary_search_with_steps([1, 3, 5, 7, 9], 4)
    
    # Test 5: First and last occurrence
    print("\n5. FIRST AND LAST OCCURRENCE")
    array_with_duplicates = [1, 2, 2, 2, 3, 4, 4, 5]
    target = 2
    
    first = binary_search_first_occurrence(array_with_duplicates, target)
    last = binary_search_last_occurrence(array_with_duplicates, target)
    first_last = binary_search_range(array_with_duplicates, target)
    
    print(f"Array: {array_with_duplicates}")
    print(f"First occurrence of {target}: index {first}")
    print(f"Last occurrence of {target}: index {last}")
    print(f"Range of {target}: {first_last}")
    
    # Test 6: Insertion point
    print("\n6. INSERTION POINT")
    sorted_arr = [1, 3, 5, 7, 9]
    values_to_insert = [0, 4, 6, 10]
    
    print(f"Original array: {sorted_arr}")
    for val in values_to_insert:
        pos = binary_search_insertion_point(sorted_arr, val)
        print(f"Insert {val} at position {pos}")
    
    # Test 7: Rotated array search
    print("\n7. SEARCH IN ROTATED SORTED ARRAY")
    rotated = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    
    result = binary_search_in_rotated_array(rotated, target)
    print(f"Rotated array: {rotated}")
    print(f"Searching for {target}: found at index {result}")
    
    # Test 8: Peak element
    print("\n8. FIND PEAK ELEMENT")
    peak_array = [1, 2, 3, 1]
    peak_index = binary_search_peak_element(peak_array)
    print(f"Array: {peak_array}")
    print(f"Peak element: {peak_array[peak_index]} at index {peak_index}")
    
    # Test 9: Square root
    print("\n9. SQUARE ROOT USING BINARY SEARCH")
    numbers = [4, 8, 15, 25, 100]
    
    for num in numbers:
        sqrt_result = binary_search_sqrt(num)
        print(f"sqrt({num}) = {sqrt_result} (since {sqrt_result}² = {sqrt_result**2})")
    
    # Test 10: Edge cases
    print("\n10. EDGE CASES")
    
    # Empty array
    empty_result = binary_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element
    single_found = binary_search([42], 42)
    single_not_found = binary_search([42], 7)
    print(f"Search 42 in [42]: {single_found}")
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Two elements
    two_elem = [1, 3]
    print(f"Search 1 in {two_elem}: {binary_search(two_elem, 1)}")
    print(f"Search 3 in {two_elem}: {binary_search(two_elem, 3)}")
    print(f"Search 2 in {two_elem}: {binary_search(two_elem, 2)}")