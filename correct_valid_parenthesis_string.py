def checkValidString(s: str) -> bool:
    min_open = 0  # Minimum possible open parentheses
    max_open = 0  # Maximum possible open parentheses
    
    for char in s:
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        else:  # char == '*'
            min_open -= 1  # Treat as ')'
            max_open += 1  # Treat as '('
        
        # If max_open becomes negative, we have too many closing parentheses
        if max_open < 0:
            return False
        
        # min_open should never go below 0 (can't have negative open parentheses)
        min_open = max(min_open, 0)
    
    # Valid if we can have exactly 0 open parentheses at the end
    return min_open <= 0 <= max_open


def checkValidString_alternative(s: str) -> bool:
    """
    Alternative solution using two passes
    """
    # First pass: left to right, treat '*' as '('
    balance = 0
    for char in s:
        if char in '(*':
            balance += 1
        else:  # char == ')'
            balance -= 1
        if balance < 0:
            return False
    
    # Second pass: right to left, treat '*' as ')'
    balance = 0
    for char in reversed(s):
        if char in ')*':
            balance += 1
        else:  # char == '('
            balance -= 1
        if balance < 0:
            return False
    
    return True


# Test cases
test_cases = [
    ("()", True),
    ("(*)", True),
    ("(*))", True),
    ("(()", False),
    ("*)", True),
    ("(*", True),
    ("**", True),
    ("(*))", True),
    ("(((*", True),
    ("*)))", False),
    ("", True),
    "*",  # Should be True
    "(**(*()**()**((**(*)",  # Complex case
]

print("Testing correct solutions:")
print("\nMethod 1 (Range tracking):")
for case in test_cases:
    if isinstance(case, tuple):
        s, expected = case
        result = checkValidString(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' -> {result} (expected: {expected})")
    else:
        result = checkValidString(case)
        print(f"'{case}' -> {result}")

print("\nMethod 2 (Two passes):")
for case in test_cases:
    if isinstance(case, tuple):
        s, expected = case
        result = checkValidString_alternative(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' -> {result} (expected: {expected})")
    else:
        result = checkValidString_alternative(case)
        print(f"'{case}' -> {result}")


# Your original solution for comparison
def your_checkValidString(s: str) -> bool:
    stack = []
    backtrack = s[0] if s else ""
    star_char = ""
    for ch in s:
        if ch == "(":
            backtrack = ch
            stack.append(")")
        elif ch == ")" and len(stack) != 0:
            backtrack = ch
            stack.pop()
        # The star condition
        else:
            if backtrack == "(":
                star_char = ")"
            elif backtrack == ")":
                star_char = "("
            else:
                star_char = ""
            if star_char == ")" and len(stack) != 0:
                stack.pop()
            elif star_char == "(":
                stack.append(")")
            else:
                if len(stack) != 0:
                    stack.pop()
    return len(stack) == 0

print("\nYour original solution:")
simple_tests = [("()", True), ("(*)", True), ("(*))", True), ("(()", False)]
for s, expected in simple_tests:
    result = your_checkValidString(s)
    status = "✓" if result == expected else "✗"
    print(f"{status} '{s}' -> {result} (expected: {expected})")