def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None


# Test the function
test_array = [-3, -2, 1, 0]
print(f"Second largest: {find_second_largest(test_array)}")  # Output: -3
