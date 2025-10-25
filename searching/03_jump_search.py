"""
JUMP SEARCH (BLOCK SEARCH)
==========================
A searching algorithm that works on SORTED arrays.
It jumps ahead by fixed steps to find a block where the target might be,
then performs linear search within that block.

Key Points:
- Array MUST be sorted
- Combines the benefits of linear search and binary search
- Optimal jump size is √n (square root of array length)

How it works:
1. Jump ahead by √n steps until we find a block where target might be
2. If we overshoot, go back to the previous block
3. Perform linear search within that block

Time Complexity: O(√n) - better than linear search, worse than binary search
Space Complexity: O(1)
"""

import math

def jump_search(arr, target):
    """
    Search for target in sorted array using jump search.
    
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
    
    # Calculate optimal jump size (square root of array length)
    jump_size = int(math.sqrt(n))
    
    # Start from beginning
    prev = 0
    
    # Jump ahead until we find a block where target might be
    while arr[min(jump_size, n) - 1] < target:
        prev = jump_size                    # Remember where we were
        jump_size += int(math.sqrt(n))      # Jump forward
        
        # If we've gone past the end of array, target doesn't exist
        if prev >= n:
            return -1
    
    # Now we know target is between prev and jump_size (if it exists)
    # Perform linear search in this block
    while arr[prev] < target:
        prev += 1
        
        # If we reach the end of current block or end of array
        if prev == min(jump_size, n):
            return -1
    
    # Check if we found the target
    if arr[prev] == target:
        return prev
    
    return -1


def jump_search_with_steps(arr, target):
    """
    Jump search with step-by-step explanation.
    Shows how the algorithm jumps and then searches linearly.
    """
    print(f"Searching for {target} in sorted array: {arr}")
    n = len(arr)
    
    if n == 0:
        print("Array is empty!")
        return -1
    
    # Calculate jump size
    jump_size = int(math.sqrt(n))
    print(f"Array length: {n}")
    print(f"Optimal jump size: √{n} = {jump_size}")
    
    prev = 0
    step = 1
    
    print("\n--- JUMPING PHASE ---")
    
    # Jumping phase
    while arr[min(jump_size, n) - 1] < target:
        print(f"Step {step}: Check position {min(jump_size, n) - 1}")
        print(f"  Value at position {min(jump_size, n) - 1}: {arr[min(jump_size, n) - 1]}")
        print(f"  {arr[min(jump_size, n) - 1]} < {target}, so jump forward")
        
        prev = jump_size
        jump_size += int(math.sqrt(n))
        step += 1
        
        if prev >= n:
            print(f"  Jumped past array end, {target} not found")
            return -1
    
    print(f"Step {step}: Check position {min(jump_size, n) - 1}")
    print(f"  Value at position {min(jump_size, n) - 1}: {arr[min(jump_size, n) - 1]}")
    print(f"  {arr[min(jump_size, n) - 1]} >= {target}, so target might be in block")
    print(f"  Target is between positions {prev} and {min(jump_size, n) - 1}")
    
    print(f"\n--- LINEAR SEARCH PHASE ---")
    print(f"Searching linearly from position {prev}")
    
    # Linear search phase
    search_step = 1
    while arr[prev] < target:
        print(f"Linear step {search_step}: Check position {prev}")
        print(f"  Value: {arr[prev]} < {target}, continue")
        
        prev += 1
        search_step += 1
        
        if prev == min(jump_size, n):
            print(f"  Reached end of block, {target} not found")
            return -1
    
    print(f"Linear step {search_step}: Check position {prev}")
    print(f"  Value: {arr[prev]}")
    
    if arr[prev] == target:
        print(f"  ✅ Found {target} at index {prev}!")
        return prev
    else:
        print(f"  ❌ {target} not found")
        return -1


def jump_search_optimized(arr, target):
    """
    Optimized version of jump search with early termination.
    """
    n = len(arr)
    
    if n == 0:
        return -1
    
    # Handle single element
    if n == 1:
        return 0 if arr[0] == target else -1
    
    jump_size = int(math.sqrt(n))
    prev = 0
    
    # Jumping phase with bounds checking
    while prev < n and arr[min(jump_size - 1, n - 1)] < target:
        prev = jump_size
        jump_size += int(math.sqrt(n))
        
        if prev >= n:
            return -1
    
    # Linear search phase with bounds checking
    end = min(jump_size, n)
    for i in range(prev, end):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return -1
    
    return -1


def jump_search_with_custom_step(arr, target, step_size):
    """
    Jump search with custom step size instead of √n.
    Useful for experimenting with different jump sizes.
    
    Args:
        arr: SORTED array
        target: Element to search for
        step_size: Custom jump size
    
    Returns:
        Index of target if found, -1 if not found
    """
    n = len(arr)
    
    if n == 0 or step_size <= 0:
        return -1
    
    prev = 0
    
    # Jump ahead by custom step size
    while prev < n and arr[min(prev + step_size - 1, n - 1)] < target:
        prev += step_size
        
        if prev >= n:
            return -1
    
    # Linear search within the block
    end = min(prev + step_size, n)
    for i in range(prev, end):
        if i < n and arr[i] == target:
            return i
        elif i < n and arr[i] > target:
            return -1
    
    return -1


def compare_jump_sizes(arr, target):
    """
    Compare different jump sizes to show their performance.
    """
    n = len(arr)
    print(f"Comparing different jump sizes for array of length {n}")
    print(f"Searching for: {target}")
    
    # Test different jump sizes
    jump_sizes = [1, 2, int(math.sqrt(n)), n//4, n//2]
    
    for size in jump_sizes:
        if size <= 0:
            continue
            
        result = jump_search_with_custom_step(arr, target, size)
        
        if size == 1:
            print(f"  Jump size {size} (linear search): {'Found' if result != -1 else 'Not found'}")
        elif size == int(math.sqrt(n)):
            print(f"  Jump size {size} (optimal √n): {'Found' if result != -1 else 'Not found'}")
        else:
            print(f"  Jump size {size}: {'Found' if result != -1 else 'Not found'}")


def jump_search_all_occurrences(arr, target):
    """
    Find all occurrences of target using jump search approach.
    
    Args:
        arr: SORTED array (may contain duplicates)
        target: Element to find all occurrences of
    
    Returns:
        List of indices where target is found
    """
    n = len(arr)
    
    if n == 0:
        return []
    
    jump_size = int(math.sqrt(n))
    prev = 0
    
    # Find the block where target might be
    while arr[min(jump_size, n) - 1] < target:
        prev = jump_size
        jump_size += int(math.sqrt(n))
        
        if prev >= n:
            return []
    
    # Find all occurrences in this block and adjacent blocks
    result = []
    
    # Search from prev to end of current block
    end = min(jump_size, n)
    for i in range(prev, end):
        if arr[i] == target:
            result.append(i)
        elif arr[i] > target:
            break
    
    return result


# Test all jump search functions
if __name__ == "__main__":
    print("=== JUMP SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic jump search
    print("1. BASIC JUMP SEARCH")
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    target = 15
    
    result = jump_search(sorted_array, target)
    print(f"Array: {sorted_array}")
    print(f"Searching for: {target}")
    print(f"Found at index: {result}")
    
    # Test 2: Jump search with steps
    print("\n2. JUMP SEARCH WITH DETAILED STEPS")
    jump_search_with_steps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 7)
    
    # Test 3: Search for non-existent element
    print("\n3. SEARCH FOR NON-EXISTENT ELEMENT")
    jump_search_with_steps([1, 3, 5, 7, 9, 11, 13], 6)
    
    # Test 4: Different array sizes
    print("\n4. DIFFERENT ARRAY SIZES")
    
    # Small array
    small_array = [1, 5, 9]
    result_small = jump_search(small_array, 5)
    print(f"Small array {small_array}: search for 5 -> index {result_small}")
    
    # Medium array
    medium_array = list(range(0, 20, 2))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    result_medium = jump_search(medium_array, 12)
    print(f"Medium array {medium_array}: search for 12 -> index {result_medium}")
    
    # Large array
    large_array = list(range(0, 100, 3))  # [0, 3, 6, 9, ...]
    result_large = jump_search(large_array, 33)
    print(f"Large array (length {len(large_array)}): search for 33 -> index {result_large}")
    
    # Test 5: Compare different jump sizes
    print("\n5. COMPARE DIFFERENT JUMP SIZES")
    test_array = list(range(0, 50, 2))  # [0, 2, 4, 6, ..., 48]
    compare_jump_sizes(test_array, 24)
    
    # Test 6: Edge cases
    print("\n6. EDGE CASES")
    
    # Empty array
    empty_result = jump_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element - found
    single_found = jump_search([42], 42)
    print(f"Search 42 in [42]: {single_found}")
    
    # Single element - not found
    single_not_found = jump_search([42], 7)
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Search for first element
    first_element = jump_search([1, 3, 5, 7, 9], 1)
    print(f"Search for first element: {first_element}")
    
    # Search for last element
    last_element = jump_search([1, 3, 5, 7, 9], 9)
    print(f"Search for last element: {last_element}")
    
    # Test 7: Array with duplicates
    print("\n7. ARRAY WITH DUPLICATES")
    array_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    target = 5
    
    all_occurrences = jump_search_all_occurrences(array_with_dups, target)
    print(f"Array: {array_with_dups}")
    print(f"All occurrences of {target}: {all_occurrences}")
    
    # Test 8: Performance comparison with different jump sizes
    print("\n8. OPTIMAL JUMP SIZE DEMONSTRATION")
    demo_array = list(range(0, 25))  # [0, 1, 2, ..., 24]
    optimal_jump = int(math.sqrt(len(demo_array)))
    
    print(f"Array length: {len(demo_array)}")
    print(f"Optimal jump size: √{len(demo_array)} = {optimal_jump}")
    print("This minimizes the total number of comparisons needed.")