def reverse_string_with_stack(s):
    """
    Reverse a string using stack (LIFO property).
    Time Complexity: O(n), Space Complexity: O(n)
    """
    # write your code here
    stack = []
    for ch in s:
        stack.append(ch)

    reversed_string = []

    # Pop from stack to get reversed order
    while stack:
        reversed_string.append(stack.pop())

    return "".join(reversed_string)


# Test the function
test_string = "hello world"
print(f"Original: {test_string}")
print(f"Reversed: {reverse_string_with_stack(test_string)}")
