def count_occurrences(arr):
    """
    Count occurrences of each element in the array.
    Time Complexity: O(n), Space Complexity: O(k) where k is unique elements
    """
    counts = {}
    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts


# Test the function
test_array = [1, 2, 2, 3, 1, 4, 2]
print(f"Element counts: {count_occurrences(test_array)}")