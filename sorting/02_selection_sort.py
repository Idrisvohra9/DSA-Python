"""
SELECTION SORT
==============
Time Complexity: O(n²) in all cases
Space Complexity: O(1)
Stable: No (doesn't maintain relative order of equal elements)

How it works:
- Find the smallest element in the unsorted portion
- Swap it with the first element of unsorted portion
- Move the boundary of sorted portion one step forward
- Repeat until entire array is sorted
"""

def selection_sort(arr):
    """
    Sorts an array using selection sort algorithm.
    
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list in ascending order
    """
    # Get the length of the array
    n = len(arr)
    
    # Outer loop: iterate through each position in the array
    # We need to fill positions 0 to n-2 (last position will be automatically correct)
    for i in range(n - 1):
        
        # Assume current position has the minimum element
        min_index = i
        
        # Inner loop: find the actual minimum in the remaining unsorted portion
        # Look through elements from position i+1 to end of array
        for j in range(i + 1, n):
            
            # If we find an element smaller than our current minimum
            if arr[j] < arr[min_index]:
                # Update the index of minimum element
                min_index = j
        
        # If we found a smaller element somewhere else
        if min_index != i:
            # Swap the minimum element with element at current position
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


def selection_sort_with_steps(arr):
    """
    Selection sort with step-by-step visualization.
    Shows how the algorithm works internally.
    """
    print(f"Starting array: {arr}")
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        print(f"\nStep {i + 1}: Looking for minimum in positions {i} to {n-1}")
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Show what we found
        print(f"  Minimum value {arr[min_index]} found at position {min_index}")
        
        # Perform swap if needed
        if min_index != i:
            print(f"  Swapping {arr[i]} (pos {i}) with {arr[min_index]} (pos {min_index})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            print(f"  No swap needed, {arr[i]} is already in correct position")
        
        print(f"  Array after step: {arr}")
    
    return arr


# Test the selection sort function
if __name__ == "__main__":
    # Test with different types of arrays
    
    # Test 1: Regular unsorted array
    test_arr1 = [64, 25, 12, 22, 11]
    print("=== BASIC SELECTION SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", selection_sort(test_arr1.copy()))
    
    # Test 2: Array with duplicates
    test_arr2 = [5, 2, 8, 2, 9, 1]
    print("\n=== WITH DUPLICATES ===")
    print("Original array:", test_arr2)
    print("Sorted array:", selection_sort(test_arr2.copy()))
    
    # Test 3: Step-by-step demonstration
    test_arr3 = [29, 10, 14, 37, 13]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    selection_sort_with_steps(test_arr3.copy())