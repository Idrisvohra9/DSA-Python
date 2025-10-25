"""
EXPONENTIAL SEARCH (DOUBLING SEARCH)
===================================
A searching algorithm that works on SORTED arrays.
It finds the range where the target might exist by exponentially increasing the bounds,
then performs binary search within that range.

Key Points:
- Array MUST be sorted
- First finds range [i, 2i] where target might be
- Then performs binary search in that range
- Useful when we don't know the array size or it's very large

How it works:
1. Start with bound = 1
2. Keep doubling the bound until arr[bound] >= target or we reach array end
3. Perform binary search between bound/2 and bound

Time Complexity: O(log n) - same as binary search
Space Complexity: O(1) for iterative binary search
"""

def exponential_search(arr, target):
    """
    Search for target in sorted array using exponential search.
    
    Args:
        arr: SORTED list of elements
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    n = len(arr)
    
    # Handle empty array
    if n == 0:
        return -1
    
    # Check if target is at first position
    if arr[0] == target:
        return 0
    
    # Find range where target might exist
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2  # Double the bound
    
    # Perform binary search in the found range
    # Range is from bound//2 to min(bound, n-1)
    return binary_search_range(arr, target, bound // 2, min(bound, n - 1))


def binary_search_range(arr, target, left, right):
    """
    Helper function: Binary search within a specific range.
    
    Args:
        arr: SORTED array
        target: Element to search for
        left: Starting index of range
        right: Ending index of range
    
    Returns:
        Index of target if found, -1 if not found
    """
    while left <= right:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1


def exponential_search_with_steps(arr, target):
    """
    Exponential search with step-by-step explanation.
    Shows how bounds are exponentially increased.
    """
    print(f"Searching for {target} in sorted array: {arr}")
    n = len(arr)
    
    if n == 0:
        print("Array is empty!")
        return -1
    
    # Check first element
    print(f"\nStep 1: Check first element")
    print(f"  arr[0] = {arr[0]}")
    if arr[0] == target:
        print(f"  ✅ Found {target} at index 0!")
        return 0
    
    print(f"  {arr[0]} != {target}, continue with exponential bounds")
    
    # Find exponential bounds
    print(f"\n--- EXPONENTIAL BOUND FINDING ---")
    bound = 1
    step = 2
    
    while bound < n and arr[bound] < target:
        print(f"Step {step}: Check bound = {bound}")
        print(f"  arr[{bound}] = {arr[bound]}")
        print(f"  {arr[bound]} < {target}, double the bound")
        bound *= 2
        step += 1
    
    # Determine final search range
    left = bound // 2
    right = min(bound, n - 1)
    
    print(f"Step {step}: Check bound = {min(bound, n-1)}")
    if bound < n:
        print(f"  arr[{bound}] = {arr[bound]}")
        print(f"  {arr[bound]} >= {target}, found range!")
    else:
        print(f"  Reached end of array at index {n-1}")
    
    print(f"  Target is between indices {left} and {right}")
    print(f"  Search range: {arr[left:right+1]}")
    
    # Binary search in the range
    print(f"\n--- BINARY SEARCH IN RANGE [{left}, {right}] ---")
    return binary_search_range_with_steps(arr, target, left, right)


def binary_search_range_with_steps(arr, target, left, right):
    """
    Binary search with steps, used by exponential search.
    """
    step = 1
    
    while left <= right:
        middle = left + (right - left) // 2
        
        print(f"Binary step {step}:")
        print(f"  Range: [{left}, {right}]")
        print(f"  Middle: {middle}, Value: {arr[middle]}")
        
        if arr[middle] == target:
            print(f"  ✅ Found {target} at index {middle}!")
            return middle
        
        elif arr[middle] > target:
            print(f"  {arr[middle]} > {target}, search left half")
            right = middle - 1
        
        else:
            print(f"  {arr[middle]} < {target}, search right half")
            left = middle + 1
        
        step += 1
    
    print(f"  ❌ {target} not found in range")
    return -1


def exponential_search_recursive(arr, target, bound=1):
    """
    Recursive version of exponential search.
    
    Args:
        arr: SORTED array
        target: Element to search for
        bound: Current exponential bound
    
    Returns:
        Index of target if found, -1 if not found
    """
    n = len(arr)
    
    # Base cases
    if n == 0:
        return -1
    
    if arr[0] == target:
        return 0
    
    # If bound is beyond array or we found our range
    if bound >= n or arr[bound] >= target:
        left = bound // 2
        right = min(bound, n - 1)
        return binary_search_range(arr, target, left, right)
    
    # Continue with doubled bound
    return exponential_search_recursive(arr, target, bound * 2)


def exponential_search_unbounded(arr, target):
    """
    Exponential search for unbounded or very large arrays.
    This version is useful when you don't know the array size.
    """
    # Start with bound = 1
    bound = 1
    
    # Keep doubling until we find a bound or get out of range
    try:
        while arr[bound] < target:
            bound *= 2
    except IndexError:
        # We've gone beyond the array
        pass
    
    # Binary search in the range [bound//2, bound]
    left = bound // 2
    right = bound
    
    while left <= right:
        try:
            middle = left + (right - left) // 2
            
            if arr[middle] == target:
                return middle
            elif arr[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
                
        except IndexError:
            # middle is beyond array, search left half
            right = middle - 1
    
    return -1


def exponential_vs_binary_search(arr, target):
    """
    Compare exponential search with regular binary search.
    Shows the different approaches and their step counts.
    """
    print(f"COMPARING EXPONENTIAL vs BINARY SEARCH")
    print(f"Array: {arr}")
    print(f"Target: {target}")
    
    # Exponential search steps
    print(f"\n--- EXPONENTIAL SEARCH ---")
    n = len(arr)
    exp_steps = 0
    
    # Count exponential bound finding steps
    bound = 1
    while bound < n and arr[bound] < target:
        exp_steps += 1
        print(f"Bound step {exp_steps}: bound = {bound}, arr[{bound}] = {arr[bound]}")
        bound *= 2
    
    if bound < n:
        print(f"Found range: [{bound//2}, {min(bound, n-1)}]")
    
    # Count binary search steps in range
    left = bound // 2
    right = min(bound, n - 1)
    binary_steps = 0
    
    while left <= right:
        binary_steps += 1
        middle = left + (right - left) // 2
        
        print(f"Binary step {binary_steps}: check index {middle}, value {arr[middle]}")
        
        if arr[middle] == target:
            print(f"Found at index {middle}!")
            break
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    total_exp_steps = exp_steps + binary_steps
    
    # Regular binary search steps
    print(f"\n--- REGULAR BINARY SEARCH ---")
    left, right = 0, len(arr) - 1
    regular_binary_steps = 0
    
    while left <= right:
        regular_binary_steps += 1
        middle = left + (right - left) // 2
        
        print(f"Step {regular_binary_steps}: check index {middle}, value {arr[middle]}")
        
        if arr[middle] == target:
            print(f"Found at index {middle}!")
            break
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    print(f"\nComparison:")
    print(f"  Exponential search: {total_exp_steps} steps ({exp_steps} exponential + {binary_steps} binary)")
    print(f"  Regular binary search: {regular_binary_steps} steps")


def exponential_search_first_occurrence(arr, target):
    """
    Find first occurrence of target using exponential search approach.
    Useful for arrays with duplicates.
    """
    n = len(arr)
    
    if n == 0:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find exponential bounds
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2
    
    # Binary search for first occurrence in range
    left = bound // 2
    right = min(bound, n - 1)
    result = -1
    
    while left <= right:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            result = middle
            right = middle - 1  # Continue searching left for first occurrence
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return result


# Test all exponential search functions
if __name__ == "__main__":
    print("=== EXPONENTIAL SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic exponential search
    print("1. BASIC EXPONENTIAL SEARCH")
    sorted_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    target = 64
    
    result = exponential_search(sorted_array, target)
    print(f"Array: {sorted_array}")
    print(f"Searching for: {target}")
    print(f"Found at index: {result}")
    
    # Test 2: Exponential search with steps
    print("\n2. EXPONENTIAL SEARCH WITH DETAILED STEPS")
    exponential_search_with_steps([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 15)
    
    # Test 3: Search for non-existent element
    print("\n3. SEARCH FOR NON-EXISTENT ELEMENT")
    exponential_search_with_steps([2, 4, 6, 8, 10, 12, 14], 9)
    
    # Test 4: Comparison with binary search
    print("\n4. EXPONENTIAL vs BINARY SEARCH COMPARISON")
    test_array = list(range(0, 32, 2))  # [0, 2, 4, 6, ..., 30]
    exponential_vs_binary_search(test_array, 20)
    
    # Test 5: Large array demonstration
    print("\n5. LARGE ARRAY DEMONSTRATION")
    large_array = list(range(0, 1000, 5))  # [0, 5, 10, 15, ..., 995]
    target = 500
    
    print(f"Large array (length {len(large_array)})")
    print(f"Searching for {target}...")
    
    result = exponential_search(large_array, target)
    print(f"Found at index: {result}")
    
    # Test 6: Edge cases
    print("\n6. EDGE CASES")
    
    # Empty array
    empty_result = exponential_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element - found
    single_found = exponential_search([42], 42)
    print(f"Search 42 in [42]: {single_found}")
    
    # Single element - not found
    single_not_found = exponential_search([42], 7)
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Target at first position
    first_element = exponential_search([1, 5, 10, 15, 20], 1)
    print(f"Search for first element: {first_element}")
    
    # Target at last position
    last_element = exponential_search([1, 5, 10, 15, 20], 20)
    print(f"Search for last element: {last_element}")
    
    # Test 7: Array with duplicates
    print("\n7. ARRAY WITH DUPLICATES")
    array_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7]
    target = 4
    
    first_occurrence = exponential_search_first_occurrence(array_with_dups, target)
    regular_result = exponential_search(array_with_dups, target)
    
    print(f"Array: {array_with_dups}")
    print(f"Regular search for {target}: index {regular_result}")
    print(f"First occurrence of {target}: index {first_occurrence}")
    
    # Test 8: Recursive version
    print("\n8. RECURSIVE EXPONENTIAL SEARCH")
    recursive_array = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    recursive_result = exponential_search_recursive(recursive_array, 18)
    print(f"Array: {recursive_array}")
    print(f"Recursive search for 18: found at index {recursive_result}")
    
    # Test 9: When exponential search is most beneficial
    print("\n9. WHEN EXPONENTIAL SEARCH IS MOST BENEFICIAL")
    print("Exponential search is particularly useful when:")
    print("- You don't know the array size in advance")
    print("- The array is very large and target is near the beginning")
    print("- You're dealing with an infinite or unbounded array")
    
    # Demonstrate with target near beginning
    beginning_array = list(range(0, 1000))  # [0, 1, 2, ..., 999]
    target_near_start = 7
    
    print(f"\nExample: Array of 1000 elements, searching for {target_near_start}")
    print("Exponential search will find the range [4, 8] quickly,")
    print("while binary search will check the entire array range [0, 999]")