"""
FIBONACCI SEARCH
===============
A comparison-based searching algorithm that works on SORTED arrays.
It uses Fibonacci numbers to divide the array into unequal parts.

Key Points:
- Array MUST be sorted
- Uses Fibonacci numbers to determine division points
- Divides array into two unequal parts (golden ratio)
- No division operations needed (only addition and subtraction)

How it works:
1. Find the smallest Fibonacci number ≥ array length
2. Use Fibonacci numbers to divide the array
3. Compare target with element at Fibonacci position
4. Eliminate portion based on comparison
5. Move to next smaller Fibonacci numbers

Time Complexity: O(log n) - similar to binary search
Space Complexity: O(1)
"""

def fibonacci_search(arr, target):
    """
    Search for target in sorted array using Fibonacci search.
    
    Args:
        arr: SORTED list of elements
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    n = len(arr)
    
    if n == 0:
        return -1
    
    # Generate Fibonacci numbers until we find one >= n
    fib_m2 = 0  # (m-2)th Fibonacci number
    fib_m1 = 1  # (m-1)th Fibonacci number
    fib_m = fib_m2 + fib_m1  # mth Fibonacci number
    
    # Find smallest Fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    # Marks the eliminated range from front
    offset = -1
    
    # While there are elements to be inspected
    while fib_m > 1:
        # Check if fib_m2 is a valid location
        i = min(offset + fib_m2, n - 1)
        
        # If target is greater than the value at index fib_m2, cut the subarray from offset to i
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        
        # If target is less than the value at index fib_m2, cut the subarray after i+1
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        
        # Element found
        else:
            return i
    
    # Comparing the last element with target
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1


def fibonacci_search_with_steps(arr, target):
    """
    Fibonacci search with step-by-step explanation.
    Shows how Fibonacci numbers are used to divide the array.
    """
    print(f"Searching for {target} in sorted array: {arr}")
    n = len(arr)
    
    if n == 0:
        print("Array is empty!")
        return -1
    
    # Generate Fibonacci sequence
    print(f"\n--- GENERATING FIBONACCI NUMBERS ---")
    fib_m2 = 0  # F(m-2)
    fib_m1 = 1  # F(m-1)
    fib_m = fib_m2 + fib_m1  # F(m)
    
    fib_sequence = [fib_m2, fib_m1]
    
    # Find smallest Fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
        fib_sequence.append(fib_m)
    
    print(f"Array length: {n}")
    print(f"Fibonacci sequence: {fib_sequence}")
    print(f"Using Fibonacci numbers: F(m-2)={fib_m2}, F(m-1)={fib_m1}, F(m)={fib_m}")
    
    offset = -1
    step = 1
    
    print(f"\n--- SEARCH PROCESS ---")
    
    while fib_m > 1:
        # Check if fib_m2 is a valid location
        i = min(offset + fib_m2, n - 1)
        
        print(f"\nStep {step}:")
        print(f"  Current Fibonacci: F(m-2)={fib_m2}, F(m-1)={fib_m1}, F(m)={fib_m}")
        print(f"  Offset: {offset}")
        print(f"  Check position: min({offset} + {fib_m2}, {n-1}) = {i}")
        print(f"  Value at position {i}: {arr[i]}")
        
        if arr[i] < target:
            print(f"  {arr[i]} < {target}, eliminate left portion")
            print(f"  Move to right: eliminate range [0, {i}]")
            
            # Move three Fibonacci numbers down
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
            
            print(f"  New Fibonacci: F(m-2)={fib_m2}, F(m-1)={fib_m1}, F(m)={fib_m}")
        
        elif arr[i] > target:
            print(f"  {arr[i]} > {target}, eliminate right portion")
            print(f"  Move to left: eliminate range [{i+1}, {n-1}]")
            
            # Move two Fibonacci numbers down
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
            
            print(f"  New Fibonacci: F(m-2)={fib_m2}, F(m-1)={fib_m1}, F(m)={fib_m}")
        
        else:
            print(f"  ✅ Found {target} at index {i}!")
            return i
        
        step += 1
    
    # Check the last remaining element
    print(f"\nFinal check:")
    if fib_m1 and offset + 1 < n:
        final_pos = offset + 1
        print(f"  Check position {final_pos}: {arr[final_pos]}")
        if arr[final_pos] == target:
            print(f"  ✅ Found {target} at index {final_pos}!")
            return final_pos
    
    print(f"  ❌ {target} not found in array")
    return -1


def generate_fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to the first number >= n.
    
    Args:
        n: Generate Fibonacci numbers until we get one >= n
    
    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    
    fib_sequence = [0, 1]
    
    while fib_sequence[-1] < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence


def fibonacci_vs_binary_search(arr, target):
    """
    Compare Fibonacci search with binary search.
    Shows different division strategies.
    """
    print(f"COMPARING FIBONACCI vs BINARY SEARCH")
    print(f"Array: {arr}")
    print(f"Target: {target}")
    
    n = len(arr)
    
    # Fibonacci search analysis
    print(f"\n--- FIBONACCI SEARCH ANALYSIS ---")
    fib_sequence = generate_fibonacci_sequence(n)
    print(f"Fibonacci sequence for array length {n}: {fib_sequence}")
    
    # Show golden ratio division
    if len(fib_sequence) >= 3:
        fib_m = fib_sequence[-1]
        fib_m1 = fib_sequence[-2]
        fib_m2 = fib_sequence[-3]
        
        ratio1 = fib_m1 / fib_m if fib_m > 0 else 0
        ratio2 = fib_m2 / fib_m1 if fib_m1 > 0 else 0
        
        print(f"Division ratios (approaching golden ratio ≈ 0.618):")
        print(f"  F(m-1)/F(m) = {fib_m1}/{fib_m} = {ratio1:.3f}")
        print(f"  F(m-2)/F(m-1) = {fib_m2}/{fib_m1} = {ratio2:.3f}")
    
    # Binary search analysis
    print(f"\n--- BINARY SEARCH ANALYSIS ---")
    print(f"Binary search always divides array in half (ratio = 0.5)")
    print(f"Each division: n → n/2 → n/4 → n/8 → ...")
    
    # Fibonacci search divisions
    print(f"\n--- DIVISION COMPARISON ---")
    print(f"Fibonacci search creates unequal divisions:")
    print(f"  Larger part ≈ 61.8% of remaining elements")
    print(f"  Smaller part ≈ 38.2% of remaining elements")
    print(f"Binary search creates equal divisions:")
    print(f"  Each part = 50% of remaining elements")


def fibonacci_search_optimized(arr, target):
    """
    Optimized version of Fibonacci search with better handling of edge cases.
    """
    n = len(arr)
    
    if n == 0:
        return -1
    
    if n == 1:
        return 0 if arr[0] == target else -1
    
    if n == 2:
        if arr[0] == target:
            return 0
        elif arr[1] == target:
            return 1
        else:
            return -1
    
    # Generate Fibonacci numbers
    fib_m2 = 0
    fib_m1 = 1
    fib_m = 1
    
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1
    
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    # Check the last element
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1


def fibonacci_search_all_occurrences(arr, target):
    """
    Find all occurrences of target using Fibonacci search approach.
    
    Args:
        arr: SORTED array that may contain duplicates
        target: Element to find all occurrences of
    
    Returns:
        List of indices where target is found
    """
    # First find any occurrence
    any_index = fibonacci_search(arr, target)
    
    if any_index == -1:
        return []
    
    # Find all occurrences by expanding left and right
    result = [any_index]
    
    # Expand left
    left = any_index - 1
    while left >= 0 and arr[left] == target:
        result.insert(0, left)
        left -= 1
    
    # Expand right
    right = any_index + 1
    while right < len(arr) and arr[right] == target:
        result.append(right)
        right += 1
    
    return result


def fibonacci_golden_ratio_demo():
    """
    Demonstrate how Fibonacci search relates to the golden ratio.
    """
    print("FIBONACCI SEARCH AND THE GOLDEN RATIO")
    print("=====================================")
    
    # Generate Fibonacci sequence
    fib = [0, 1]
    for i in range(2, 15):
        fib.append(fib[i-1] + fib[i-2])
    
    print("Fibonacci sequence:", fib[1:11])  # Skip first 0
    
    # Calculate ratios
    print("\nRatios of consecutive Fibonacci numbers:")
    golden_ratio = (1 + 5**0.5) / 2  # ≈ 1.618
    
    for i in range(2, 10):
        ratio = fib[i+1] / fib[i]
        error = abs(ratio - golden_ratio)
        print(f"  F({i+1})/F({i}) = {fib[i+1]}/{fib[i]} = {ratio:.6f} (error: {error:.6f})")
    
    print(f"\nGolden ratio φ = {golden_ratio:.6f}")
    print(f"1/φ = {1/golden_ratio:.6f} ≈ 0.618")
    
    print("\nFibonacci search uses this ratio to divide arrays optimally!")


# Test all Fibonacci search functions
if __name__ == "__main__":
    print("=== FIBONACCI SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic Fibonacci search
    print("1. BASIC FIBONACCI SEARCH")
    sorted_array = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85
    
    result = fibonacci_search(sorted_array, target)
    print(f"Array: {sorted_array}")
    print(f"Searching for: {target}")
    print(f"Found at index: {result}")
    
    # Test 2: Fibonacci search with steps
    print("\n2. FIBONACCI SEARCH WITH DETAILED STEPS")
    fibonacci_search_with_steps([1, 3, 5, 7, 9, 11, 13, 15], 11)
    
    # Test 3: Search for non-existent element
    print("\n3. SEARCH FOR NON-EXISTENT ELEMENT")
    fibonacci_search_with_steps([2, 4, 6, 8, 10, 12, 14], 9)
    
    # Test 4: Comparison with binary search
    print("\n4. FIBONACCI vs BINARY SEARCH COMPARISON")
    test_array = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    fibonacci_vs_binary_search(test_array, 25)
    
    # Test 5: Golden ratio demonstration
    print("\n5. GOLDEN RATIO DEMONSTRATION")
    fibonacci_golden_ratio_demo()
    
    # Test 6: Different array sizes
    print("\n6. DIFFERENT ARRAY SIZES")
    
    # Small arrays
    for size in [1, 2, 3, 5, 8, 13]:
        test_arr = list(range(1, size + 1))
        target = size // 2 + 1 if size > 1 else 1
        
        result = fibonacci_search(test_arr, target)
        fib_seq = generate_fibonacci_sequence(size)
        
        print(f"  Size {size}: {test_arr}")
        print(f"    Fibonacci numbers: {fib_seq}")
        print(f"    Search for {target}: index {result}")
    
    # Test 7: Edge cases
    print("\n7. EDGE CASES")
    
    # Empty array
    empty_result = fibonacci_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element
    single_found = fibonacci_search([42], 42)
    single_not_found = fibonacci_search([42], 7)
    print(f"Search 42 in [42]: {single_found}")
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Two elements
    two_found_first = fibonacci_search([1, 5], 1)
    two_found_second = fibonacci_search([1, 5], 5)
    two_not_found = fibonacci_search([1, 5], 3)
    print(f"Search 1 in [1, 5]: {two_found_first}")
    print(f"Search 5 in [1, 5]: {two_found_second}")
    print(f"Search 3 in [1, 5]: {two_not_found}")
    
    # Test 8: Array with duplicates
    print("\n8. ARRAY WITH DUPLICATES")
    array_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    target = 2
    
    all_occurrences = fibonacci_search_all_occurrences(array_with_dups, target)
    print(f"Array: {array_with_dups}")
    print(f"All occurrences of {target}: {all_occurrences}")
    
    # Test 9: Performance characteristics
    print("\n9. PERFORMANCE CHARACTERISTICS")
    
    sizes = [10, 20, 50, 100]
    
    for size in sizes:
        fib_seq = generate_fibonacci_sequence(size)
        fib_count = len(fib_seq) - 1  # Exclude the last one that's >= size
        
        import math
        binary_max = math.ceil(math.log2(size))
        
        print(f"  Array size {size}:")
        print(f"    Fibonacci numbers needed: {fib_count}")
        print(f"    Binary search max iterations: {binary_max}")
        print(f"    Fibonacci search max iterations: ≈ {fib_count}")
    
    # Test 10: When to use Fibonacci search
    print("\n10. WHEN TO USE FIBONACCI SEARCH")
    print("Fibonacci search is useful when:")
    print("- Division operations are expensive")
    print("- You want to avoid floating-point arithmetic")
    print("- Working with processors that handle addition/subtraction better than division")
    print("- The array access pattern needs to be more predictable")
    print("\nHowever, binary search is usually preferred because:")
    print("- Simpler to implement and understand")
    print("- Fewer edge cases to handle")
    print("- More predictable performance")
    print("- Modern processors handle division efficiently")