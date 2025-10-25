def sum_of_evens(arr):
    """
    Find the sum of all even numbers in the array.
    """
    if not arr:
        return 0

    even_sum = 0
    for num in arr:
        if num % 2 == 0:
            even_sum += num
    return even_sum

# Test the function
test_array = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print(f"Sum of even numbers: {sum_of_evens(test_array)}")  # Output: 30