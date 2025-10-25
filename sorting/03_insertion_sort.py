"""
INSERTION SORT
==============
Time Complexity: O(n²) worst/average case, O(n) best case
Space Complexity: O(1)
Stable: Yes (maintains relative order of equal elements)

How it works:
- Start with second element (assume first is sorted)
- Take current element and find its correct position in sorted portion
- Shift all larger elements one position right
- Insert current element in its correct position
- Repeat for all remaining elements
"""

def insertion_sort(arr):
    """
    Sorts an array using insertion sort algorithm.
    
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list in ascending order
    """
    # Start from second element (index 1)
    # First element (index 0) is considered already sorted
    for i in range(1, len(arr)):
        
        # Current element to be positioned correctly
        key = arr[i]
        
        # Start comparing with element just before current element
        j = i - 1
        
        # Move all elements greater than key one position ahead
        # Continue until we find correct position for key or reach beginning
        while j >= 0 and arr[j] > key:
            
            # Shift the larger element one position to the right
            arr[j + 1] = arr[j]
            
            # Move to the previous element
            j -= 1
        
        # Insert the key at its correct position
        # j+1 is the correct position because loop stopped when:
        # either j became -1 OR arr[j] <= key
        arr[j + 1] = key
    
    return arr


def insertion_sort_with_steps(arr):
    """
    Insertion sort with step-by-step visualization.
    Shows how elements are inserted into their correct positions.
    """
    print(f"Starting array: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"\nStep {i}: Inserting {key} into sorted portion {arr[:i]}")
        
        # Show the shifting process
        original_j = j
        while j >= 0 and arr[j] > key:
            print(f"  {arr[j]} > {key}, shifting {arr[j]} right")
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key
        arr[j + 1] = key
        print(f"  Inserting {key} at position {j + 1}")
        print(f"  Array after step: {arr}")
    
    return arr


def insertion_sort_recursive(arr, n=None):
    """
    Recursive implementation of insertion sort.
    
    Args:
        arr: List to sort
        n: Number of elements to sort (used for recursion)
    """
    # Base case: if array has 1 or 0 elements, it's already sorted
    if n is None:
        n = len(arr)
    
    if n <= 1:
        return arr
    
    # Recursively sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert the nth element at its correct position
    last = arr[n - 1]
    j = n - 2
    
    # Move elements that are greater than last one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    # Place last element at its correct position
    arr[j + 1] = last
    
    return arr


# Test the insertion sort functions
if __name__ == "__main__":
    # Test 1: Basic insertion sort
    test_arr1 = [12, 11, 13, 5, 6]
    print("=== BASIC INSERTION SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", insertion_sort(test_arr1.copy()))
    
    # Test 2: Already sorted array (best case)
    test_arr2 = [1, 2, 3, 4, 5]
    print("\n=== ALREADY SORTED (BEST CASE) ===")
    print("Original array:", test_arr2)
    print("Sorted array:", insertion_sort(test_arr2.copy()))
    
    # Test 3: Reverse sorted array (worst case)
    test_arr3 = [5, 4, 3, 2, 1]
    print("\n=== REVERSE SORTED (WORST CASE) ===")
    print("Original array:", test_arr3)
    print("Sorted array:", insertion_sort(test_arr3.copy()))
    
    # Test 4: Step-by-step demonstration
    test_arr4 = [5, 2, 4, 6, 1, 3]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    insertion_sort_with_steps(test_arr4.copy())
    
    # Test 5: Recursive implementation
    test_arr5 = [64, 34, 25, 12, 22, 11, 90]
    print("\n=== RECURSIVE INSERTION SORT ===")
    print("Original array:", test_arr5)
    print("Sorted array:", insertion_sort_recursive(test_arr5.copy()))