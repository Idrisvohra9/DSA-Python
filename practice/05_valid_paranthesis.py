def is_balanced_parentheses(s: str) -> bool:
    """
    Check if parentheses in string are balanced using stack.
    Time Complexity: O(n), Space Complexity: O(n)
    """
    stack = []
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
            
    return len(stack) == 0

# Test the function
test_strings = ["((()))", "(()", "())", "(())()", "((()(())))", "())(", "", "())("]
for test in test_strings:
    print(f"'{test}' is balanced: {is_balanced_parentheses(test)}")
