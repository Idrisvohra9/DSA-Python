"""
RADIX SORT
==========
Time Complexity: O(d x (n + k)) where d is number of digits, k is range of digits
Space Complexity: O(n + k)
Stable: Yes (maintains relative order of equal elements)

How it works:
- Sort numbers digit by digit starting from least significant digit (LSD)
- Use a stable sorting algorithm (like counting sort) for each digit
- Process all digits from rightmost to leftmost
- Works by sorting on each digit position while maintaining stability

Key concepts:
- LSD (Least Significant Digit): Start from rightmost digit
- MSD (Most Significant Digit): Start from leftmost digit
- Uses counting sort as subroutine for each digit
"""

def radix_sort(arr):
    """
    Sorts an array using radix sort algorithm (LSD version).
    Works with non-negative integers.
    
    Args:
        arr: List of non-negative integers
    Returns:
        Sorted list in ascending order
    """
    if not arr:
        return arr
    
    # Find the maximum number to determine number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    # exp represents the current digit position (1, 10, 100, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_for_radix(arr, exp):
    """
    Counting sort modified for radix sort.
    Sorts array according to the digit represented by exp.
    
    Args:
        arr: Array to sort
        exp: Exponent representing current digit position
    """
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits 0-9
    
    # Store count of occurrences of each digit
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    
    # Change count[i] to actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    # Process from right to left to maintain stability
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copy the output array back to arr[]
    for i in range(n):
        arr[i] = output[i]


def radix_sort_msd(arr, start=0, end=None, exp=None):
    """
    Most Significant Digit (MSD) radix sort.
    Sorts from leftmost digit to rightmost digit.
    
    Args:
        arr: Array to sort
        start: Starting index
        end: Ending index
        exp: Current digit position
    """
    if end is None:
        end = len(arr) - 1
    
    if exp is None:
        # Find maximum number and calculate highest digit position
        max_num = max(arr[start:end + 1])
        exp = 1
        while max_num // exp >= 10:
            exp *= 10
    
    # Base case: if only one element or no more digits
    if start >= end or exp < 1:
        return
    
    # Count array for digits 0-9
    count = [0] * 10
    
    # Count occurrences of each digit
    for i in range(start, end + 1):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    
    # Convert counts to starting positions
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    output = [0] * (end - start + 1)
    for i in range(end, start - 1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copy back to original array
    for i in range(start, end + 1):
        arr[i] = output[i - start]
    
    # Recursively sort each bucket
    prev_count = 0
    for i in range(10):
        if count[i] > prev_count:
            radix_sort_msd(arr, start + prev_count, start + count[i] - 1, exp // 10)
        prev_count = count[i]


def radix_sort_with_steps(arr):
    """
    Radix sort with step-by-step visualization.
    Shows the sorting process for each digit position.
    """
    if not arr:
        return arr
    
    print(f"Original array: {arr}")
    max_num = max(arr)
    print(f"Maximum number: {max_num}")
    
    exp = 1
    step = 1
    
    while max_num // exp > 0:
        print(f"\n=== STEP {step}: Sorting by digit at position {exp} ===")
        
        # Show which digit we're sorting by
        print("Digits being sorted:")
        for num in arr:
            digit = (num // exp) % 10
            print(f"  {num} -> digit {digit}")
        
        # Perform counting sort for this digit
        counting_sort_for_radix(arr, exp)
        print(f"Array after sorting by digit at position {exp}: {arr}")
        
        exp *= 10
        step += 1
    
    print(f"\nFinal sorted array: {arr}")
    return arr


def radix_sort_strings(arr):
    """
    Radix sort adapted for strings of equal length.
    Sorts strings lexicographically.
    
    Args:
        arr: List of strings of equal length
    Returns:
        Sorted list of strings
    """
    if not arr or not arr[0]:
        return arr
    
    # All strings should have the same length
    max_len = len(arr[0])
    
    # Sort by each character position from right to left
    for pos in range(max_len - 1, -1, -1):
        counting_sort_for_strings(arr, pos)
    
    return arr


def counting_sort_for_strings(arr, pos):
    """
    Counting sort for strings based on character at given position.
    
    Args:
        arr: Array of strings
        pos: Character position to sort by
    """
    n = len(arr)
    output = [""] * n
    count = [0] * 256  # ASCII characters
    
    # Count frequency of each character
    for string in arr:
        if pos < len(string):
            count[ord(string[pos])] += 1
    
    # Calculate cumulative count
    for i in range(1, 256):
        count[i] += count[i - 1]
    
    # Build output array (process from right to maintain stability)
    for i in range(n - 1, -1, -1):
        string = arr[i]
        if pos < len(string):
            char_code = ord(string[pos])
            output[count[char_code] - 1] = string
            count[char_code] -= 1
    
    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort_negative_numbers(arr):
    """
    Radix sort adapted to handle negative numbers.
    
    Args:
        arr: List of integers (can include negative numbers)
    Returns:
        Sorted list
    """
    if not arr:
        return arr
    
    # Separate positive and negative numbers
    negative = [-x for x in arr if x < 0]  # Convert to positive
    positive = [x for x in arr if x >= 0]
    
    # Sort both arrays
    if negative:
        radix_sort(negative)
        negative = [-x for x in reversed(negative)]  # Convert back and reverse
    
    if positive:
        radix_sort(positive)
    
    # Combine results
    return negative + positive


def get_digit_count(num):
    """
    Helper function to count digits in a number.
    
    Args:
        num: Integer number
    Returns:
        Number of digits
    """
    if num == 0:
        return 1
    
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# Test the radix sort functions
if __name__ == "__main__":
    # Test 1: Basic radix sort
    test_arr1 = [170, 45, 75, 90, 2, 802, 24, 66]
    print("=== BASIC RADIX SORT ===")
    print("Original array:", test_arr1)
    print("Sorted array:", radix_sort(test_arr1.copy()))
    
    # Test 2: Array with different digit lengths
    test_arr2 = [1, 23, 456, 7890, 12, 345]
    print("\n=== DIFFERENT DIGIT LENGTHS ===")
    print("Original array:", test_arr2)
    print("Sorted array:", radix_sort(test_arr2.copy()))
    
    # Test 3: Array with same digits
    test_arr3 = [121, 432, 564, 23, 1, 45, 788]
    print("\n=== MIXED NUMBERS ===")
    print("Original array:", test_arr3)
    print("Sorted array:", radix_sort(test_arr3.copy()))
    
    # Test 4: String sorting
    test_strings = ["abc", "def", "aaa", "xyz", "bcd"]
    print("\n=== STRING SORTING ===")
    print("Original strings:", test_strings)
    print("Sorted strings:", radix_sort_strings(test_strings.copy()))
    
    # Test 5: Negative numbers
    test_arr5 = [-5, 3, -2, 8, -1, 6, 0]
    print("\n=== WITH NEGATIVE NUMBERS ===")
    print("Original array:", test_arr5)
    print("Sorted array:", radix_sort_negative_numbers(test_arr5))
    
    # Test 6: Step-by-step demonstration
    test_arr6 = [329, 457, 657, 839, 436, 720, 355]
    print("\n=== STEP-BY-STEP DEMONSTRATION ===")
    radix_sort_with_steps(test_arr6.copy())
    
    # Test 7: Edge cases
    print("\n=== EDGE CASES ===")
    print("Empty array:", radix_sort([]))
    print("Single element:", radix_sort([42]))
    print("Already sorted:", radix_sort([1, 2, 3, 4, 5]))
    print("All same numbers:", radix_sort([7, 7, 7, 7]))