"""
QUICK SORT
==========
Time Complexity: O(n log n) average case, O(n²) worst case
Space Complexity: O(log n) average case, O(n) worst case
Stable: No (doesn't maintain relative order of equal elements)

How it works:
- Choose a 'pivot' element from the array
- Partition: rearrange array so elements smaller than pivot come before it,
  and elements greater come after it
- Recursively apply quick sort to sub-arrays on both sides of pivot
- Uses "divide and conquer" strategy
"""

def quick_sort(arr):
    """
    Sorts an array using quick sort algorithm.
    
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list in ascending order
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (we'll use the middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts:
    # 1. Elements less than pivot
    left = [x for x in arr if x < pivot]
    
    # 2. Elements equal to pivot
    middle = [x for x in arr if x == pivot]
    
    # 3. Elements greater than pivot
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right parts, then combine
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr, low=0, high=None):
    """
    In-place version of quick sort (modifies original array).
    More memory efficient as it doesn't create new arrays.
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
    """
    if high is None:
        high = len(arr) - 1
    
    # Only proceed if there are at least 2 elements to sort
    if low < high:
        
        # Partition the array and get the pivot index
        # After partitioning, pivot is in its correct final position
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort_in_place(arr, low, pivot_index - 1)    # Sort left side
        quick_sort_in_place(arr, pivot_index + 1, high)   # Sort right side


def partition(arr, low, high):
    """
    Partitions the array around a pivot element.
    Uses Lomuto partition scheme.
    
    Args:
        arr: Array to partition
        low: Starting index
        high: Ending index
    Returns:
        Index of pivot after partitioning
    """
    # Choose the last element as pivot
    pivot = arr[high]
    
    # Index of smaller element (indicates right position of pivot)
    i = low - 1
    
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            
            # Increment index of smaller element
            i += 1
            
            # Swap current element with element at i
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return position of pivot
    return i + 1


def quick_sort_hoare_partition(arr, low=0, high=None):
    """
    Quick sort using Hoare partition scheme.
    This is the original partitioning scheme by Tony Hoare.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array using Hoare scheme
        pivot_index = hoare_partition(arr, low, high)
        
        # Recursively sort both parts
        quick_sort_hoare_partition(arr, low, pivot_index)
        quick_sort_hoare_partition(arr, pivot_index + 1, high)


def hoare_partition(arr, low, high):
    """
    Hoare partition scheme.
    More efficient than Lomuto partition.
    """
    # Choose first element as pivot
    pivot = arr[low]
    
    # Initialize pointers
    i = low - 1
    j = high + 1
    
    while True:
        # Find element on left that should be on right
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Find element on right that should be on left
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        # If elements crossed, partitioning is done
        if i >= j:
            return j
        
        # Swap elements
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_with_steps(arr, depth=0):
    """
    Quick sort with step-by-step visualization.
    Shows the partitioning process.
    """
    indent = "  " * depth
    print(f"{indent}Sorting: {arr}")
    
    if len(arr) <= 1:
        print(f"{indent}Base case: {arr}")
        return arr
    
    pivot = arr[len(arr) // 2]
    print(f"{indent}Pivot chosen: {pivot}")
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{indent}Partitioned: left={left}, middle={middle}, right={right}")
    
    left_sorted = quick_sort_with_steps(left, depth + 1)
    right_sorted = quick_sort_with_steps(right, depth + 1)
    
    result = left_sorted + middle + right_sorted
    print(f"{indent}Combined result: {result}")
    
    return result


def quick_sort_random_pivot(arr):
    """
    Quick sort with random pivot selection.
    Helps avoid worst-case performance on already sorted arrays.
    """
    import random
    
    if len(arr) <= 1:
        return arr
    
    # Choose random pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_random_pivot(left) + middle + quick_sort_random_pivot(right)


# Test the quick sort functions
if __name__ == "__main__":
    # Test 1: Basic quick sort
    test_arr1 = [10, 7, 8, 9, 1, 5]
    print("=== BASIC QUICK SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", quick_sort(test_arr1))
    
    # Test 2: In-place quick sort
    test_arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("\n=== IN-PLACE QUICK SORT ===")
    print("Original array:", test_arr2)
    quick_sort_in_place(test_arr2)
    print("Sorted array:", test_arr2)
    
    # Test 3: Hoare partition quick sort
    test_arr3 = [5, 2, 8, 6, 1, 9, 4]
    print("\n=== HOARE PARTITION QUICK SORT ===")
    print("Original array:", test_arr3)
    quick_sort_hoare_partition(test_arr3)
    print("Sorted array:", test_arr3)
    
    # Test 4: Already sorted array (potential worst case)
    test_arr4 = [1, 2, 3, 4, 5, 6, 7]
    print("\n=== ALREADY SORTED (POTENTIAL WORST CASE) ===")
    print("Original array:", test_arr4)
    print("Sorted array:", quick_sort(test_arr4))
    
    # Test 5: Random pivot quick sort
    test_arr5 = [3, 6, 8, 10, 1, 2, 1]
    print("\n=== RANDOM PIVOT QUICK SORT ===")
    print("Original array:", test_arr5)
    print("Sorted array:", quick_sort_random_pivot(test_arr5))
    
    # Test 6: Step-by-step demonstration
    test_arr6 = [6, 3, 8, 5, 2, 7, 1, 4]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    quick_sort_with_steps(test_arr6)