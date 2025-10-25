"""
BUBBLE SORT
===========
Time Complexity: O(n²) worst/average case, O(n) best case
Space Complexity: O(1)
Stable: Yes (maintains relative order of equal elements)

How it works:
- Compare adjacent elements and swap if they're in wrong order
- After each pass, the largest element "bubbles up" to the end
- Repeat until no more swaps are needed
"""

def bubble_sort(arr):
    """
    Sorts an array using bubble sort algorithm.
    
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list in ascending order
    """
    # Get the length of the array
    n = len(arr)
    
    # Outer loop: controls number of passes
    # We need at most n-1 passes to sort n elements
    for i in range(n):
        
        # Flag to track if any swaps happened in this pass
        # If no swaps occur, the array is already sorted
        swapped = False
        
        # Inner loop: compare adjacent elements
        # Last i elements are already in their correct position
        # So we only need to check first (n-i-1) elements
        for j in range(0, n - i - 1):
            
            # Compare current element with next element
            # If current is greater than next, they're in wrong order
            if arr[j] > arr[j + 1]:
                
                # Swap the elements to fix the order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # Mark that we made a swap
                swapped = True
        
        # If no swaps were made in this pass,
        # the array is already sorted, so we can stop early
        if not swapped:
            break
    
    return arr


# Test the bubble sort function
if __name__ == "__main__":
    # Test with different types of arrays
    
    # Test 1: Regular unsorted array
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr1)
    print("Sorted array:", bubble_sort(test_arr1.copy()))
    
    # Test 2: Already sorted array (best case)
    test_arr2 = [1, 2, 3, 4, 5]
    print("\nAlready sorted:", test_arr2)
    print("Sorted array:", bubble_sort(test_arr2.copy()))
    
    # Test 3: Reverse sorted array (worst case)
    test_arr3 = [5, 4, 3, 2, 1]
    print("\nReverse sorted:", test_arr3)
    print("Sorted array:", bubble_sort(test_arr3.copy()))
    
    # Test 4: Array with duplicates
    test_arr4 = [3, 7, 3, 1, 7, 1]
    print("\nWith duplicates:", test_arr4)
    print("Sorted array:", bubble_sort(test_arr4.copy()))