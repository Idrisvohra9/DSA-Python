"""
TERNARY SEARCH
=============
A divide-and-conquer searching algorithm that works on SORTED arrays.
It divides the array into THREE parts instead of two (like binary search).

Key Points:
- Array MUST be sorted
- Divides search space into three equal parts
- Uses two middle points instead of one
- More comparisons per iteration than binary search

How it works:
1. Calculate two middle points: mid1 and mid2
2. If target equals mid1 or mid2, we found it!
3. If target < mid1, search the first third
4. If target > mid2, search the last third
5. Otherwise, search the middle third
6. Repeat until found or no more elements

Time Complexity: O(log₃ n) ≈ O(log n) - similar to binary search but with more comparisons
Space Complexity: O(1) for iterative version, O(log n) for recursive version
"""

def ternary_search(arr, target):
    """
    Search for target in sorted array using ternary search (iterative version).
    
    Args:
        arr: SORTED list of elements
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Calculate two middle points
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Check if target is at either middle point
        if arr[mid1] == target:
            return mid1
        
        if arr[mid2] == target:
            return mid2
        
        # Determine which third to search
        if target < arr[mid1]:
            # Target is in first third
            right = mid1 - 1
        
        elif target > arr[mid2]:
            # Target is in last third
            left = mid2 + 1
        
        else:
            # Target is in middle third
            left = mid1 + 1
            right = mid2 - 1
    
    return -1


def ternary_search_recursive(arr, target, left=0, right=None):
    """
    Ternary search using recursion.
    
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
    
    # Calculate two middle points
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    # Check if target is at either middle point
    if arr[mid1] == target:
        return mid1
    
    if arr[mid2] == target:
        return mid2
    
    # Recursive calls for different thirds
    if target < arr[mid1]:
        # Search first third
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    
    elif target > arr[mid2]:
        # Search last third
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    
    else:
        # Search middle third
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)


def ternary_search_with_steps(arr, target):
    """
    Ternary search with step-by-step explanation.
    Shows how the search space gets divided into three parts.
    """
    print(f"Searching for {target} in sorted array: {arr}")
    
    left = 0
    right = len(arr) - 1
    step = 1
    
    while left <= right:
        # Calculate two middle points
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"\nStep {step}:")
        print(f"  Search area: indices {left} to {right}")
        print(f"  Search area values: {arr[left:right+1]}")
        print(f"  Mid1 index: {mid1}, Mid1 value: {arr[mid1]}")
        print(f"  Mid2 index: {mid2}, Mid2 value: {arr[mid2]}")
        print(f"  Three sections:")
        print(f"    First:  [{left}, {mid1-1}] = {arr[left:mid1] if mid1 > left else '[]'}")
        print(f"    Middle: [{mid1+1}, {mid2-1}] = {arr[mid1+1:mid2] if mid2 > mid1+1 else '[]'}")
        print(f"    Last:   [{mid2+1}, {right}] = {arr[mid2+1:right+1] if right > mid2 else '[]'}")
        
        # Check if target is at either middle point
        if arr[mid1] == target:
            print(f"  ✅ Found {target} at mid1 index {mid1}!")
            return mid1
        
        if arr[mid2] == target:
            print(f"  ✅ Found {target} at mid2 index {mid2}!")
            return mid2
        
        # Determine which third to search
        if target < arr[mid1]:
            print(f"  {target} < {arr[mid1]}, search FIRST third")
            right = mid1 - 1
        
        elif target > arr[mid2]:
            print(f"  {target} > {arr[mid2]}, search LAST third")
            left = mid2 + 1
        
        else:
            print(f"  {arr[mid1]} < {target} < {arr[mid2]}, search MIDDLE third")
            left = mid1 + 1
            right = mid2 - 1
        
        step += 1
    
    print(f"  ❌ {target} not found in array")
    return -1


def ternary_vs_binary_search(arr, target):
    """
    Compare ternary search with binary search.
    Shows the number of comparisons and iterations for each.
    """
    print(f"COMPARING TERNARY vs BINARY SEARCH")
    print(f"Array: {arr}")
    print(f"Target: {target}")
    
    # Ternary search
    print(f"\n--- TERNARY SEARCH ---")
    left, right = 0, len(arr) - 1
    ternary_iterations = 0
    ternary_comparisons = 0
    
    while left <= right:
        ternary_iterations += 1
        
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"Iteration {ternary_iterations}: Check positions {mid1} and {mid2}")
        print(f"  Values: {arr[mid1]} and {arr[mid2]}")
        
        # Count comparisons
        ternary_comparisons += 1  # Compare with mid1
        if arr[mid1] == target:
            print(f"  Found at mid1!")
            break
        
        ternary_comparisons += 1  # Compare with mid2
        if arr[mid2] == target:
            print(f"  Found at mid2!")
            break
        
        ternary_comparisons += 1  # Compare target < mid1
        if target < arr[mid1]:
            print(f"  Search first third")
            right = mid1 - 1
        else:
            ternary_comparisons += 1  # Compare target > mid2
            if target > arr[mid2]:
                print(f"  Search last third")
                left = mid2 + 1
            else:
                print(f"  Search middle third")
                left = mid1 + 1
                right = mid2 - 1
    
    # Binary search
    print(f"\n--- BINARY SEARCH ---")
    left, right = 0, len(arr) - 1
    binary_iterations = 0
    binary_comparisons = 0
    
    while left <= right:
        binary_iterations += 1
        
        mid = left + (right - left) // 2
        
        print(f"Iteration {binary_iterations}: Check position {mid}")
        print(f"  Value: {arr[mid]}")
        
        binary_comparisons += 1  # Compare with mid
        if arr[mid] == target:
            print(f"  Found!")
            break
        
        binary_comparisons += 1  # Compare target < mid
        if arr[mid] > target:
            print(f"  Search left half")
            right = mid - 1
        else:
            print(f"  Search right half")
            left = mid + 1
    
    print(f"\nComparison Results:")
    print(f"  Ternary search: {ternary_iterations} iterations, {ternary_comparisons} comparisons")
    print(f"  Binary search:  {binary_iterations} iterations, {binary_comparisons} comparisons")
    
    # Theoretical analysis
    import math
    n = len(arr)
    ternary_theoretical = math.ceil(math.log(n) / math.log(3))
    binary_theoretical = math.ceil(math.log(n) / math.log(2))
    
    print(f"\nTheoretical maximum iterations:")
    print(f"  Ternary: ⌈log₃({n})⌉ = {ternary_theoretical}")
    print(f"  Binary:  ⌈log₂({n})⌉ = {binary_theoretical}")


def ternary_search_peak_finding(arr):
    """
    Use ternary search to find a peak element in an array.
    A peak is an element that is greater than or equal to its neighbors.
    
    Args:
        arr: Array of numbers (not necessarily sorted)
    
    Returns:
        Index of a peak element
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Compare the two middle elements
        if arr[mid1] < arr[mid2]:
            # Peak is more likely in the right portion
            left = mid1 + 1
        else:
            # Peak is more likely in the left portion
            right = mid2 - 1
    
    return left


def ternary_search_minimum_rotated(arr):
    """
    Find minimum element in a rotated sorted array using ternary search.
    
    Args:
        arr: Rotated sorted array
    
    Returns:
        Index of minimum element
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # If array is already sorted
        if arr[left] <= arr[right]:
            return left
        
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # The minimum is in the unsorted part
        if arr[mid1] > arr[right]:
            left = mid1 + 1
        elif arr[mid2] > arr[right]:
            left = mid1 + 1
            right = mid2
        else:
            right = mid1
    
    return left


def ternary_search_range(arr, target):
    """
    Find all occurrences of target using ternary search approach.
    
    Args:
        arr: SORTED array that may contain duplicates
        target: Element to find all occurrences of
    
    Returns:
        Tuple of (first_index, last_index) or (-1, -1) if not found
    """
    # Find any occurrence first
    any_occurrence = ternary_search(arr, target)
    
    if any_occurrence == -1:
        return (-1, -1)
    
    # Find first occurrence
    left = 0
    right = any_occurrence
    first = any_occurrence
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            first = mid1
            right = mid1 - 1
        elif arr[mid2] == target:
            first = mid2
            right = mid2 - 1
        elif arr[mid1] < target:
            left = mid1 + 1
        else:
            right = mid1 - 1
    
    # Find last occurrence
    left = any_occurrence
    right = len(arr) - 1
    last = any_occurrence
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid2] == target:
            last = mid2
            left = mid2 + 1
        elif arr[mid1] == target:
            last = mid1
            left = mid1 + 1
        elif arr[mid2] > target:
            right = mid2 - 1
        else:
            left = mid2 + 1
    
    return (first, last)


# Test all ternary search functions
if __name__ == "__main__":
    print("=== TERNARY SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic ternary search
    print("1. BASIC TERNARY SEARCH")
    sorted_array = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
    target = 16
    
    result = ternary_search(sorted_array, target)
    print(f"Array: {sorted_array}")
    print(f"Searching for: {target}")
    print(f"Found at index: {result}")
    
    # Test 2: Ternary search with steps
    print("\n2. TERNARY SEARCH WITH DETAILED STEPS")
    ternary_search_with_steps([2, 5, 8, 11, 14, 17, 20, 23], 14)
    
    # Test 3: Search for non-existent element
    print("\n3. SEARCH FOR NON-EXISTENT ELEMENT")
    ternary_search_with_steps([1, 3, 5, 7, 9, 11], 6)
    
    # Test 4: Comparison with binary search
    print("\n4. TERNARY vs BINARY SEARCH COMPARISON")
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    ternary_vs_binary_search(test_array, 15)
    
    # Test 5: Recursive version
    print("\n5. RECURSIVE TERNARY SEARCH")
    recursive_array = [10, 20, 30, 40, 50, 60, 70, 80]
    recursive_result = ternary_search_recursive(recursive_array, 50)
    print(f"Array: {recursive_array}")
    print(f"Recursive search for 50: found at index {recursive_result}")
    
    # Test 6: Edge cases
    print("\n6. EDGE CASES")
    
    # Empty array
    empty_result = ternary_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element - found
    single_found = ternary_search([42], 42)
    print(f"Search 42 in [42]: {single_found}")
    
    # Single element - not found
    single_not_found = ternary_search([42], 7)
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Two elements
    two_elem = [1, 3]
    print(f"Search 1 in {two_elem}: {ternary_search(two_elem, 1)}")
    print(f"Search 3 in {two_elem}: {ternary_search(two_elem, 3)}")
    
    # Three elements
    three_elem = [1, 5, 9]
    print(f"Search 5 in {three_elem}: {ternary_search(three_elem, 5)}")
    
    # Test 7: Array with duplicates
    print("\n7. ARRAY WITH DUPLICATES")
    array_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    target = 2
    
    range_result = ternary_search_range(array_with_dups, target)
    print(f"Array: {array_with_dups}")
    print(f"Range of {target}: {range_result}")
    
    # Test 8: Peak finding (special application)
    print("\n8. PEAK FINDING USING TERNARY SEARCH")
    peak_array = [1, 3, 20, 4, 1, 0]  # Peak at index 2
    peak_index = ternary_search_peak_finding(peak_array)
    print(f"Array: {peak_array}")
    print(f"Peak element: {peak_array[peak_index]} at index {peak_index}")
    
    # Test 9: Performance analysis
    print("\n9. PERFORMANCE ANALYSIS")
    
    large_array = list(range(0, 81))  # 81 elements (3^4)
    target = 60
    
    print(f"Array size: {len(large_array)} elements")
    print(f"Searching for: {target}")
    
    # Calculate theoretical iterations
    import math
    n = len(large_array)
    ternary_max = math.ceil(math.log(n) / math.log(3))
    binary_max = math.ceil(math.log(n) / math.log(2))
    
    print(f"Maximum iterations:")
    print(f"  Ternary search: ⌈log₃({n})⌉ = {ternary_max}")
    print(f"  Binary search:  ⌈log₂({n})⌉ = {binary_max}")
    print(f"  But ternary search makes more comparisons per iteration!")
    
    # Test 10: When to use ternary search
    print("\n10. WHEN TO USE TERNARY SEARCH")
    print("Ternary search is useful when:")
    print("- You want to minimize the number of iterations (depth of recursion)")
    print("- Comparison operations are very fast")
    print("- You're working with mathematical functions (finding minimum/maximum)")
    print("- The cost of iteration setup is high compared to comparisons")
    print("\nHowever, binary search is generally preferred because:")
    print("- Fewer total comparisons needed")
    print("- Simpler implementation")
    print("- Better constant factors in practice")