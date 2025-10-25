"""
MERGE SORT
==========
Time Complexity: O(n log n) in all cases
Space Complexity: O(n)
Stable: Yes (maintains relative order of equal elements)

How it works:
- Divide: Split array into two halves recursively until single elements
- Conquer: Merge the sorted halves back together in sorted order
- Uses "divide and conquer" strategy
- Very consistent performance regardless of input
"""

def merge_sort(arr):
    """
    Sorts an array using merge sort algorithm.
    
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list in ascending order
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: find the middle point to split array into two halves
    mid = len(arr) // 2
    
    # Recursively sort both halves
    left_half = merge_sort(arr[:mid])    # Sort left half
    right_half = merge_sort(arr[mid:])   # Sort right half
    
    # Conquer: merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
    Returns:
        Merged sorted array
    """
    # Result array to store merged elements
    result = []
    
    # Pointers for left and right arrays
    i = j = 0
    
    # Compare elements from both arrays and add smaller one to result
    while i < len(left) and j < len(right):
        
        # If left element is smaller or equal, add it to result
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1  # Move left pointer forward
        else:
            # Right element is smaller, add it to result
            result.append(right[j])
            j += 1  # Move right pointer forward
    
    # Add remaining elements from left array (if any)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right array (if any)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


def merge_sort_in_place(arr, left=0, right=None):
    """
    In-place version of merge sort (modifies original array).
    Uses less memory but still needs O(n) space for merging.
    
    Args:
        arr: Array to sort
        left: Starting index
        right: Ending index
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: if left >= right, subarray has 0 or 1 element
    if left < right:
        
        # Find middle point
        mid = (left + right) // 2
        
        # Recursively sort both halves
        merge_sort_in_place(arr, left, mid)      # Sort left half
        merge_sort_in_place(arr, mid + 1, right) # Sort right half
        
        # Merge the sorted halves
        merge_in_place(arr, left, mid, right)


def merge_in_place(arr, left, mid, right):
    """
    Merges two sorted subarrays in place.
    Left subarray: arr[left...mid]
    Right subarray: arr[mid+1...right]
    """
    # Create temporary arrays for left and right subarrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    # Pointers for left_arr, right_arr, and main array
    i = j = 0
    k = left
    
    # Merge elements back into original array
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left_arr
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements from right_arr
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort_with_steps(arr, depth=0):
    """
    Merge sort with visualization of the divide and conquer process.
    """
    indent = "  " * depth
    print(f"{indent}Dividing: {arr}")
    
    if len(arr) <= 1:
        print(f"{indent}Base case reached: {arr}")
        return arr
    
    mid = len(arr) // 2
    print(f"{indent}Split at index {mid}")
    
    left_half = merge_sort_with_steps(arr[:mid], depth + 1)
    right_half = merge_sort_with_steps(arr[mid:], depth + 1)
    
    result = merge(left_half, right_half)
    print(f"{indent}Merging {left_half} + {right_half} = {result}")
    
    return result


# Test the merge sort functions
if __name__ == "__main__":
    # Test 1: Basic merge sort
    test_arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== BASIC MERGE SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", merge_sort(test_arr1))
    
    # Test 2: In-place merge sort
    test_arr2 = [12, 11, 13, 5, 6, 7]
    print("\n=== IN-PLACE MERGE SORT ===")
    print("Original array:", test_arr2)
    merge_sort_in_place(test_arr2)
    print("Sorted array:", test_arr2)
    
    # Test 3: Already sorted array
    test_arr3 = [1, 2, 3, 4, 5]
    print("\n=== ALREADY SORTED ===")
    print("Original array:", test_arr3)
    print("Sorted array:", merge_sort(test_arr3))
    
    # Test 4: Array with duplicates
    test_arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("\n=== WITH DUPLICATES ===")
    print("Original array:", test_arr4)
    print("Sorted array:", merge_sort(test_arr4))
    
    # Test 5: Step-by-step demonstration
    test_arr5 = [6, 5, 3, 1, 8, 7, 2, 4]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    merge_sort_with_steps(test_arr5)