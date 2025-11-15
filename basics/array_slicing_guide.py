"""
Python Array Slicing and Splicing Guide
=======================================

This guide covers all the essential concepts of list slicing and manipulation in Python.
"""

# =============================================================================
# 1. BASIC SLICING SYNTAX
# =============================================================================

print("=" * 50)
print("1. BASIC SLICING SYNTAX")
print("=" * 50)

# Basic syntax: list[start:stop:step]
# - start: starting index (inclusive)
# - stop: ending index (exclusive)
# - step: step size (default is 1)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original array: {arr}")
# print("".s)
# Basic slicing examples
print("arr[2:7]     =", arr[2:7])      # Elements from index 2 to 6
print("arr[:5]      =", arr[:5])       # First 5 elements
print("arr[3:]      =", arr[3:])       # Elements from index 3 to end
print("arr[:]       =", arr[:])        # Entire array (creates a copy)
print("arr[-3:]     =", arr[-3:])      # Last 3 elements
print("arr[:-2]     =", arr[:-2])      # All except last 2 elements
print("arr[-5:-1]   =", arr[-5:-1])    # From 5th last to 2nd last
print()

# =============================================================================
# 2. STEP PARAMETER
# =============================================================================

print("=" * 50)
print("2. STEP PARAMETER")
print("=" * 50)

print("arr[::2]     =", arr[::2])      # Every 2nd element
print("arr[1::2]    =", arr[1::2])     # Every 2nd element starting from index 1
print("arr[::3]     =", arr[::3])      # Every 3rd element
print("arr[::-1]    =", arr[::-1])     # Reverse the entire array
print("arr[7:2:-1]  =", arr[7:2:-1])   # From index 7 to 3 (backwards)
print("arr[8:1:-2]  =", arr[8:1:-2])   # From index 8 to 2, step -2
print()

# =============================================================================
# 3. NEGATIVE INDEXING
# =============================================================================

print("=" * 50)
print("3. NEGATIVE INDEXING")
print("=" * 50)

print("Index mapping for negative indices:")
for i in range(len(arr)):
    print(f"arr[{i}] = arr[{i-len(arr)}] = {arr[i]}")
print()

print("arr[-1]      =", arr[-1])       # Last element
print("arr[-3:-1]   =", arr[-3:-1])    # 3rd last to 2nd last
print("arr[:-3]     =", arr[:-3])      # All except last 3
print("arr[-7:-2]   =", arr[-7:-2])    # From 7th last to 3rd last
print()

# =============================================================================
# 4. SLICING FOR MODIFICATION (SPLICING)
# =============================================================================

print("=" * 50)
print("4. SLICING FOR MODIFICATION (SPLICING)")
print("=" * 50)

# Replace elements using slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")

# Replace a slice with new values
numbers[2:5] = [20, 30, 40]
print(f"After numbers[2:5] = [20, 30, 40]: {numbers}")

# Insert elements (empty slice)
numbers[3:3] = [25, 35]
print(f"After numbers[3:3] = [25, 35]: {numbers}")

# Delete elements (assign empty list)
numbers[2:4] = []
print(f"After numbers[2:4] = []: {numbers}")

# Replace with different length
numbers[1:3] = [100, 200, 300, 400]
print(f"After numbers[1:3] = [100, 200, 300, 400]: {numbers}")

# Replace every other element
# numbers[::2] = [1000, 2000, 3000, 4000]
# print(f"After numbers[::2] = [1000, 2000, 3000, 4000]: {numbers}")
print()

# =============================================================================
# 5. COMMON PATTERNS AND TRICKS
# =============================================================================

print("=" * 50)
print("5. COMMON PATTERNS AND TRICKS")
print("=" * 50)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original data: {data}")
print()

print("Common patterns:")
print(f"First half: data[:len(data)//2] = {data[:len(data)//2]}")
print(f"Second half: data[len(data)//2:] = {data[len(data)//2:]}")
print(f"Middle element(s): data[len(data)//2-1:len(data)//2+1] = {data[len(data)//2-1:len(data)//2+1]}")
print(f"Reverse: data[::-1] = {data[::-1]}")
print(f"Every 2nd from start: data[::2] = {data[::2]}")
print(f"Every 2nd from 2nd element: data[1::2] = {data[1::2]}")
print()

# =============================================================================
# 6. STRING SLICING (SAME RULES APPLY)
# =============================================================================

print("=" * 50)
print("6. STRING SLICING (SAME RULES APPLY)")
print("=" * 50)

text = "Hello World!"
print(f"Original string: '{text}'")
print()

print(f"text[6:]     = '{text[6:]}'")     # From index 6 to end
print(f"text[:5]     = '{text[:5]}'")     # First 5 characters
print(f"text[::2]    = '{text[::2]}'")    # Every 2nd character
print(f"text[::-1]   = '{text[::-1]}'")   # Reverse string
print(f"text[2:8:2]  = '{text[2:8:2]}'")  # From 2 to 7, step 2
print()

# =============================================================================
# 7. IMPORTANT NOTES AND GOTCHAS
# =============================================================================

print("=" * 50)
print("7. IMPORTANT NOTES AND GOTCHAS")
print("=" * 50)

print("Important points to remember:")
print("1. Slicing creates a NEW list/string (shallow copy)")
print("2. Original list is unchanged unless you assign back")
print("3. Out of range indices don't raise errors in slicing")
print("4. Step cannot be 0")
print("5. When step is negative, start should be > stop")
print()

# Demonstrating shallow copy
original = [1, 2, 3, 4, 5]
sliced = original[1:4]
print(f"Original: {original}")
print(f"Sliced: {sliced}")
sliced[0] = 999
print(f"After modifying sliced[0]: Original={original}, Sliced={sliced}")
print()

# Out of range doesn't error
print("Out of range examples:")
print(f"original[100:200] = {original[100:200]}")  # Returns empty list
print(f"original[2:100] = {original[2:100]}")      # Returns from 2 to end
print()

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("=" * 50)
print("8. PRACTICAL EXAMPLES")
print("=" * 50)

def rotate_array_right(arr, k):
    """Rotate array to the right by k positions"""
    k = k % len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k]

def rotate_array_left(arr, k):
    """Rotate array to the left by k positions"""
    k = k % len(arr)
    return arr[k:] + arr[:k]

def reverse_words(sentence):
    """Reverse each word in a sentence"""
    return ' '.join(word[::-1] for word in sentence.split())

def get_middle_elements(arr):
    """Get middle element(s) of an array"""
    mid = len(arr) // 2
    if len(arr) % 2 == 1:
        return [arr[mid]]
    else:
        return arr[mid-1:mid+1]

# Test the functions
test_arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original array: {test_arr}")
print(f"Rotate right by 3: {rotate_array_right(test_arr, 3)}")
print(f"Rotate left by 2: {rotate_array_left(test_arr, 2)}")
print()

test_sentence = "Hello World Python"
print(f"Original: '{test_sentence}'")
print(f"Reversed words: '{reverse_words(test_sentence)}'")
print()

print(f"Middle of [1,2,3,4,5]: {get_middle_elements([1,2,3,4,5])}")
print(f"Middle of [1,2,3,4]: {get_middle_elements([1,2,3,4])}")