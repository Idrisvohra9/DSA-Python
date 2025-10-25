"""
HEAP SORT
=========
Time Complexity: O(n log n) in all cases
Space Complexity: O(1)
Stable: No (doesn't maintain relative order of equal elements)

How it works:
- Build a max heap from the input array
- Repeatedly extract the maximum element (root) and place it at the end
- Restore heap property after each extraction
- Uses the heap data structure for efficient sorting

Key concepts:
- Heap: Complete binary tree where parent >= children (max heap)
- Array representation: for node at index i:
  - Left child: 2*i + 1
  - Right child: 2*i + 2
  - Parent: (i-1)//2
"""

def heap_sort(arr):
    """
    Sorts an array using heap sort algorithm.
    
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list in ascending order
    """
    n = len(arr)
    
    # Step 1: Build max heap from the array
    # Start from last non-leaf node and heapify downwards
    # Last non-leaf node is at index (n//2 - 1)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        
        # Move current root (maximum) to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call heapify on the reduced heap
        # (exclude the last i elements which are already sorted)
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    Ensures the heap property: parent >= children
    
    Args:
        arr: Array representing the heap
        n: Size of heap
        i: Root index of subtree to heapify
    """
    # Initialize largest as root
    largest = i
    
    # Calculate indices of left and right children
    left = 2 * i + 1      # Left child
    right = 2 * i + 2     # Right child
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        # Swap root with largest element
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Builds a max heap from an unsorted array.
    
    Args:
        arr: Array to convert to max heap
    """
    n = len(arr)
    
    # Start from last non-leaf node and heapify all nodes
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort_with_steps(arr):
    """
    Heap sort with step-by-step visualization.
    Shows the heap building and extraction process.
    """
    print(f"Original array: {arr}")
    n = len(arr)
    
    # Step 1: Build max heap
    print("\n=== BUILDING MAX HEAP ===")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Heapifying subtree rooted at index {i}")
        heapify(arr, n, i)
        print(f"Array after heapifying index {i}: {arr}")
    
    print(f"\nMax heap built: {arr}")
    
    # Step 2: Extract elements
    print("\n=== EXTRACTING ELEMENTS ===")
    for i in range(n - 1, 0, -1):
        print(f"\nStep {n - i}: Extracting maximum")
        print(f"  Before: {arr}")
        print(f"  Swapping {arr[0]} (root) with {arr[i]} (last unsorted)")
        
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        print(f"  After swap: {arr}")
        print(f"  Sorted portion: {arr[i:]} | Unsorted heap: {arr[:i]}")
        
        # Heapify reduced heap
        heapify(arr, i, 0)
        print(f"  After heapify: {arr}")
    
    print(f"\nFinal sorted array: {arr}")
    return arr


def is_heap(arr, i=0, n=None):
    """
    Check if array represents a valid max heap.
    
    Args:
        arr: Array to check
        i: Current index (root of subtree)
        n: Size of heap
    Returns:
        True if valid heap, False otherwise
    """
    if n is None:
        n = len(arr)
    
    # If leaf node, it's a valid heap
    if i >= n // 2:
        return True
    
    # Check if current node satisfies heap property
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check left child
    if left < n and arr[i] < arr[left]:
        return False
    
    # Check right child
    if right < n and arr[i] < arr[right]:
        return False
    
    # Recursively check subtrees
    return (is_heap(arr, left, n) and 
            is_heap(arr, right, n))


def heap_sort_iterative(arr):
    """
    Iterative version of heapify (avoids recursion stack overflow).
    """
    def heapify_iterative(arr, n, i):
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest == i:
                break
            
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
    
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_iterative(arr, n, i)
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_iterative(arr, i, 0)
    
    return arr


# Test the heap sort functions
if __name__ == "__main__":
    # Test 1: Basic heap sort
    test_arr1 = [12, 11, 13, 5, 6, 7]
    print("=== BASIC HEAP SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", heap_sort(test_arr1.copy()))
    
    # Test 2: Array with duplicates
    test_arr2 = [4, 10, 3, 5, 1, 3, 10, 1]
    print("\n=== WITH DUPLICATES ===")
    print("Original array:", test_arr2)
    print("Sorted array:", heap_sort(test_arr2.copy()))
    
    # Test 3: Already sorted array
    test_arr3 = [1, 2, 3, 4, 5, 6]
    print("\n=== ALREADY SORTED ===")
    print("Original array:", test_arr3)
    print("Sorted array:", heap_sort(test_arr3.copy()))
    
    # Test 4: Reverse sorted array
    test_arr4 = [6, 5, 4, 3, 2, 1]
    print("\n=== REVERSE SORTED ===")
    print("Original array:", test_arr4)
    print("Sorted array:", heap_sort(test_arr4.copy()))
    
    # Test 5: Check heap property
    test_heap = [10, 8, 9, 4, 7, 5, 3, 1, 2, 6]
    print("\n=== HEAP VALIDATION ===")
    print("Array:", test_heap)
    print("Is valid max heap:", is_heap(test_heap))
    
    # Test 6: Step-by-step demonstration
    test_arr6 = [4, 10, 3, 5, 1]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    heap_sort_with_steps(test_arr6.copy())