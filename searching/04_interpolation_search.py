"""
INTERPOLATION SEARCH
===================
An advanced searching algorithm that works on SORTED and UNIFORMLY DISTRIBUTED arrays.
It estimates where the target might be located based on the values at the ends.

Key Points:
- Array MUST be sorted AND uniformly distributed
- Uses interpolation formula to estimate target position
- Better than binary search for uniformly distributed data

How it works:
1. Estimate target position using interpolation formula
2. If target matches estimated position, we found it!
3. If target is smaller, search the left portion
4. If target is larger, search the right portion
5. Repeat until found or search space is exhausted

Time Complexity: O(log log n) for uniformly distributed data, O(n) worst case
Space Complexity: O(1)
"""

def interpolation_search(arr, target):
    """
    Search for target in sorted, uniformly distributed array using interpolation.
    
    Args:
        arr: SORTED list with uniformly distributed elements
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    # Keep searching while target might be in current range
    while left <= right and target >= arr[left] and target <= arr[right]:
        
        # If we have only one element
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Interpolation formula to estimate position
        # pos = left + [(target - arr[left]) / (arr[right] - arr[left])] * (right - left)
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        
        # Found the target!
        if arr[pos] == target:
            return pos
        
        # Target is in the left portion
        if arr[pos] > target:
            right = pos - 1
        
        # Target is in the right portion
        else:
            left = pos + 1
    
    return -1


def interpolation_search_with_steps(arr, target):
    """
    Interpolation search with step-by-step explanation.
    Shows how the position is estimated using interpolation formula.
    """
    print(f"Searching for {target} in array: {arr}")
    print("Using INTERPOLATION SEARCH (estimating position)")
    
    left = 0
    right = len(arr) - 1
    step = 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        print(f"\nStep {step}:")
        print(f"  Search range: indices {left} to {right}")
        print(f"  Values: {arr[left]} to {arr[right]}")
        
        if left == right:
            if arr[left] == target:
                print(f"  ✅ Found {target} at index {left}!")
                return left
            else:
                print(f"  ❌ {target} not found")
                return -1
        
        # Show interpolation calculation
        print(f"  Interpolation formula:")
        print(f"    pos = {left} + [({target} - {arr[left]}) / ({arr[right]} - {arr[left]})] * ({right} - {left})")
        
        fraction = (target - arr[left]) / (arr[right] - arr[left])
        pos = left + int(fraction * (right - left))
        
        print(f"    pos = {left} + [{target - arr[left]} / {arr[right] - arr[left]}] * {right - left}")
        print(f"    pos = {left} + {fraction:.3f} * {right - left}")
        print(f"    pos = {left} + {fraction * (right - left):.1f} = {pos}")
        
        # Ensure position is within bounds
        pos = max(left, min(pos, right))
        print(f"  Estimated position: {pos}, Value: {arr[pos]}")
        
        if arr[pos] == target:
            print(f"  ✅ Found {target} at index {pos}!")
            return pos
        
        elif arr[pos] > target:
            print(f"  {arr[pos]} > {target}, search LEFT portion")
            right = pos - 1
        
        else:
            print(f"  {arr[pos]} < {target}, search RIGHT portion")
            left = pos + 1
        
        step += 1
    
    print(f"  ❌ {target} not found (outside search range)")
    return -1


def interpolation_search_recursive(arr, target, left=0, right=None):
    """
    Recursive version of interpolation search.
    
    Args:
        arr: SORTED array with uniform distribution
        target: Element to search for
        left: Starting index of current search range
        right: Ending index of current search range
    
    Returns:
        Index of target if found, -1 if not found
    """
    if right is None:
        right = len(arr) - 1
    
    # Base cases
    if left > right or target < arr[left] or target > arr[right]:
        return -1
    
    if left == right:
        return left if arr[left] == target else -1
    
    # Calculate interpolation position
    pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
    
    # Ensure position is within bounds
    pos = max(left, min(pos, right))
    
    if arr[pos] == target:
        return pos
    elif arr[pos] > target:
        return interpolation_search_recursive(arr, target, left, pos - 1)
    else:
        return interpolation_search_recursive(arr, target, pos + 1, right)


def interpolation_vs_binary_search(arr, target):
    """
    Compare interpolation search with binary search.
    Shows the different approaches to position estimation.
    """
    print(f"COMPARING INTERPOLATION vs BINARY SEARCH")
    print(f"Array: {arr}")
    print(f"Target: {target}")
    
    # Interpolation search steps
    print(f"\n--- INTERPOLATION SEARCH ---")
    left, right = 0, len(arr) - 1
    interp_steps = 0
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        interp_steps += 1
        
        if left == right:
            break
        
        # Interpolation position
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        pos = max(left, min(pos, right))
        
        print(f"Step {interp_steps}: Check position {pos} (value: {arr[pos]})")
        
        if arr[pos] == target:
            print(f"Found at position {pos}!")
            break
        elif arr[pos] > target:
            right = pos - 1
        else:
            left = pos + 1
    
    # Binary search steps
    print(f"\n--- BINARY SEARCH ---")
    left, right = 0, len(arr) - 1
    binary_steps = 0
    
    while left <= right:
        binary_steps += 1
        
        # Binary search always takes middle
        pos = left + (right - left) // 2
        
        print(f"Step {binary_steps}: Check position {pos} (value: {arr[pos]})")
        
        if arr[pos] == target:
            print(f"Found at position {pos}!")
            break
        elif arr[pos] > target:
            right = pos - 1
        else:
            left = pos + 1
    
    print(f"\nComparison:")
    print(f"  Interpolation search: {interp_steps} steps")
    print(f"  Binary search: {binary_steps} steps")


def interpolation_search_with_bounds_check(arr, target):
    """
    Safer version of interpolation search with better bounds checking.
    Handles edge cases and non-uniform distributions better.
    """
    if not arr:
        return -1
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Check if target is outside the current range
        if target < arr[left] or target > arr[right]:
            return -1
        
        # If range has only one element
        if left == right:
            return left if arr[left] == target else -1
        
        # Avoid division by zero
        if arr[right] == arr[left]:
            # If all elements in range are equal
            if arr[left] == target:
                return left
            else:
                return -1
        
        # Calculate interpolation position with bounds checking
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        
        # Ensure position is within current bounds
        pos = max(left, min(pos, right))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] > target:
            right = pos - 1
        else:
            left = pos + 1
    
    return -1


def test_uniform_distribution(arr):
    """
    Test if an array has approximately uniform distribution.
    Interpolation search works best with uniform distribution.
    """
    if len(arr) < 2:
        return True, "Too few elements to determine"
    
    # Calculate differences between consecutive elements
    differences = []
    for i in range(1, len(arr)):
        differences.append(arr[i] - arr[i-1])
    
    # Check if differences are approximately equal
    avg_diff = sum(differences) / len(differences)
    max_deviation = max(abs(diff - avg_diff) for diff in differences)
    
    # If max deviation is less than 20% of average, consider it uniform
    threshold = 0.2 * avg_diff
    is_uniform = max_deviation <= threshold
    
    return is_uniform, f"Average difference: {avg_diff:.2f}, Max deviation: {max_deviation:.2f}"


# Test all interpolation search functions
if __name__ == "__main__":
    print("=== INTERPOLATION SEARCH DEMONSTRATIONS ===\n")
    
    # Test 1: Basic interpolation search on uniform data
    print("1. BASIC INTERPOLATION SEARCH (Uniform Distribution)")
    uniform_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 70
    
    result = interpolation_search(uniform_array, target)
    print(f"Array: {uniform_array}")
    print(f"Searching for: {target}")
    print(f"Found at index: {result}")
    
    # Test 2: Interpolation search with steps
    print("\n2. INTERPOLATION SEARCH WITH DETAILED STEPS")
    interpolation_search_with_steps([5, 10, 15, 20, 25, 30, 35, 40], 25)
    
    # Test 3: Comparison with binary search
    print("\n3. INTERPOLATION vs BINARY SEARCH COMPARISON")
    test_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    interpolation_vs_binary_search(test_array, 14)
    
    # Test 4: Non-uniform distribution
    print("\n4. NON-UNIFORM DISTRIBUTION")
    non_uniform = [1, 2, 4, 8, 16, 32, 64, 128]  # Powers of 2
    
    is_uniform, details = test_uniform_distribution(non_uniform)
    print(f"Array: {non_uniform}")
    print(f"Is uniform? {is_uniform} ({details})")
    
    result_non_uniform = interpolation_search_with_steps(non_uniform, 16)
    
    # Test 5: Perfect uniform distribution
    print("\n5. PERFECT UNIFORM DISTRIBUTION")
    perfect_uniform = list(range(0, 100, 10))  # [0, 10, 20, 30, ...]
    
    is_uniform, details = test_uniform_distribution(perfect_uniform)
    print(f"Array: {perfect_uniform}")
    print(f"Is uniform? {is_uniform} ({details})")
    
    result_perfect = interpolation_search(perfect_uniform, 60)
    print(f"Search for 60: found at index {result_perfect}")
    
    # Test 6: Edge cases
    print("\n6. EDGE CASES")
    
    # Empty array
    empty_result = interpolation_search([], 5)
    print(f"Search in empty array: {empty_result}")
    
    # Single element
    single_found = interpolation_search([42], 42)
    single_not_found = interpolation_search([42], 7)
    print(f"Search 42 in [42]: {single_found}")
    print(f"Search 7 in [42]: {single_not_found}")
    
    # Target outside range
    outside_small = interpolation_search([10, 20, 30], 5)
    outside_large = interpolation_search([10, 20, 30], 35)
    print(f"Search 5 in [10, 20, 30]: {outside_small}")
    print(f"Search 35 in [10, 20, 30]: {outside_large}")
    
    # All elements equal
    all_equal = interpolation_search_with_bounds_check([5, 5, 5, 5], 5)
    print(f"Search 5 in [5, 5, 5, 5]: {all_equal}")
    
    # Test 7: Recursive version
    print("\n7. RECURSIVE INTERPOLATION SEARCH")
    recursive_array = [1, 5, 9, 13, 17, 21, 25, 29]
    recursive_result = interpolation_search_recursive(recursive_array, 17)
    print(f"Array: {recursive_array}")
    print(f"Recursive search for 17: found at index {recursive_result}")
    
    # Test 8: Performance demonstration
    print("\n8. PERFORMANCE DEMONSTRATION")
    large_uniform = list(range(0, 1000, 5))  # [0, 5, 10, 15, ..., 995]
    
    print(f"Large uniform array (length {len(large_uniform)})")
    print(f"Searching for 500...")
    
    # Count steps for interpolation search
    left, right = 0, len(large_uniform) - 1
    steps = 0
    target = 500
    
    while left <= right and target >= large_uniform[left] and target <= large_uniform[right]:
        steps += 1
        if left == right:
            break
        
        pos = left + int(((target - large_uniform[left]) / 
                         (large_uniform[right] - large_uniform[left])) * (right - left))
        pos = max(left, min(pos, right))
        
        if large_uniform[pos] == target:
            break
        elif large_uniform[pos] > target:
            right = pos - 1
        else:
            left = pos + 1
    
    print(f"Interpolation search completed in {steps} steps")
    print(f"Binary search would take approximately {len(large_uniform).bit_length() - 1} steps")