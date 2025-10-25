"""
LINEAR SEARCH
=============
The simplest searching algorithm that checks every element one by one.
It works on both sorted and unsorted arrays.

How it works:
- Start from the first element
- Compare each element with the target value
- If found, return the index
- If not found after checking all elements, return -1

Time Complexity: O(n) - worst case we check all elements
Space Complexity: O(1) - only uses a constant amount of extra space
"""

def linear_search(arr, target):
    """
    Search for target element in array using linear search.
    
    Args:
        arr: List of elements to search in
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    # Go through each element in the array
    for i in range(len(arr)):
        # If current element matches target, we found it!
        if arr[i] == target:
            return i
    
    # If we reach here, target was not found
    return -1


def linear_search_with_steps(arr, target):
    """
    Linear search with step-by-step explanation.
    Shows what happens at each step.
    """
    print(f"Searching for {target} in array: {arr}")
    
    # Check each element one by one
    for i in range(len(arr)):
        current_element = arr[i]
        print(f"Step {i + 1}: Checking index {i}, value = {current_element}")
        
        # Compare current element with target
        if current_element == target:
            print(f"✅ Found {target} at index {i}!")
            return i
        else:
            print(f"   {current_element} ≠ {target}, continue searching...")
    
    # Target not found
    print(f"❌ {target} not found in array")
    return -1


def linear_search_all_occurrences(arr, target):
    """
    Find all positions where target appears in the array.
    
    Args:
        arr: List of elements to search in
        target: Element we're looking for
    
    Returns:
        List of all indices where target is found
    """
    indices = []  # Store all positions where target is found
    
    # Check every element in the array
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  # Add this position to our list
    
    return indices


def linear_search_with_condition(arr, condition_func):
    """
    Search for first element that satisfies a given condition.
    This is a more flexible version of linear search.
    
    Args:
        arr: List of elements to search in
        condition_func: Function that returns True for the element we want
    
    Returns:
        Index of first element satisfying condition, -1 if none found
    
    Example:
        # Find first even number
        linear_search_with_condition([1, 3, 8, 5, 2], lambda x: x % 2 == 0)
    """
    for i in range(len(arr)):
        # Check if current element satisfies our condition
        if condition_func(arr[i]):
            return i
    
    return -1


def linear_search_from_end(arr, target):
    """
    Linear search starting from the end of array.
    Useful when target is more likely to be near the end.
    
    Args:
        arr: List of elements to search in
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    # Start from the last element and go backwards
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    
    return -1


def linear_search_count(arr, target):
    """
    Count how many times target appears in the array.
    
    Args:
        arr: List of elements to search in
        target: Element to count
    
    Returns:
        Number of times target appears in array
    """
    count = 0
    
    # Check every element
    for element in arr:
        if element == target:
            count += 1  # Increment counter when we find target
    
    return count


def linear_search_min_max(arr):
    """
    Find minimum and maximum elements using linear search approach.
    
    Args:
        arr: List of numbers
    
    Returns:
        Tuple of (min_value, max_value, min_index, max_index)
    """
    if not arr:  # Empty array
        return None, None, -1, -1
    
    # Initialize with first element
    min_value = max_value = arr[0]
    min_index = max_index = 0
    
    # Check remaining elements
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
        elif arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    
    return min_value, max_value, min_index, max_index


# Test the linear search functions
if __name__ == "__main__":
    print("=== LINEAR SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic linear search
    print("1. BASIC LINEAR SEARCH")
    test_array = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    
    result = linear_search(test_array, target)
    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in array")
    
    # Test 2: Linear search with steps
    print("\n2. LINEAR SEARCH WITH STEPS")
    linear_search_with_steps([5, 2, 8, 1, 9], 8)
    
    # Test 3: Search for non-existent element
    print("\n3. SEARCHING FOR NON-EXISTENT ELEMENT")
    linear_search_with_steps([1, 3, 5, 7, 9], 4)
    
    # Test 4: Find all occurrences
    print("\n4. FIND ALL OCCURRENCES")
    array_with_duplicates = [1, 3, 7, 3, 9, 3, 5]
    target = 3
    indices = linear_search_all_occurrences(array_with_duplicates, target)
    print(f"Array: {array_with_duplicates}")
    print(f"All occurrences of {target}: {indices}")
    
    # Test 5: Search with condition
    print("\n5. SEARCH WITH CONDITION")
    numbers = [1, 3, 8, 5, 2, 7, 4]
    
    # Find first even number
    even_index = linear_search_with_condition(numbers, lambda x: x % 2 == 0)
    if even_index != -1:
        print(f"First even number: {numbers[even_index]} at index {even_index}")
    
    # Find first number greater than 5
    large_index = linear_search_with_condition(numbers, lambda x: x > 5)
    if large_index != -1:
        print(f"First number > 5: {numbers[large_index]} at index {large_index}")
    
    # Test 6: Search from end
    print("\n6. SEARCH FROM END")
    test_array = [1, 2, 3, 4, 3, 2, 1]
    target = 3
    
    normal_search = linear_search(test_array, target)
    reverse_search = linear_search_from_end(test_array, target)
    
    print(f"Array: {test_array}")
    print(f"First occurrence of {target}: index {normal_search}")
    print(f"Last occurrence of {target}: index {reverse_search}")
    
    # Test 7: Count occurrences
    print("\n7. COUNT OCCURRENCES")
    array = [1, 2, 3, 2, 4, 2, 5]
    target = 2
    count = linear_search_count(array, target)
    print(f"Array: {array}")
    print(f"Number {target} appears {count} times")
    
    # Test 8: Find min and max
    print("\n8. FIND MIN AND MAX")
    numbers = [64, 34, 25, 12, 22, 11, 90]
    min_val, max_val, min_idx, max_idx = linear_search_min_max(numbers)
    print(f"Array: {numbers}")
    print(f"Minimum: {min_val} at index {min_idx}")
    print(f"Maximum: {max_val} at index {max_idx}")
    
    # Test 9: Edge cases
    print("\n9. EDGE CASES")
    
    # Empty array
    empty_result = linear_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element array
    single_found = linear_search([42], 42)
    single_not_found = linear_search([42], 7)
    print(f"Search 42 in [42]: {single_found}")
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Array with one element repeated
    repeated = [5, 5, 5, 5, 5]
    all_fives = linear_search_all_occurrences(repeated, 5)
    print(f"All occurrences of 5 in {repeated}: {all_fives}")