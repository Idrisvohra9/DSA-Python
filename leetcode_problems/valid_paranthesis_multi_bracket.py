def is_balanced_parentheses(s: str) -> bool:
    stack = []
    mapping = {"(": ")", "{": "}", "[": "]"}
    # print("The shit", s)
    for ch in s:
        # print(stack)
        if ch in mapping:
            # push the expected closing bracket
            stack.append(mapping[ch])
        else:
            # if stack empty OR top doesn't match current closing, invalid
            # print("Popping this shit", stack[-1])
            if len(stack) == 0 or stack.pop() != ch:
                return False

    # stack must be empty at the end
    return len(stack) == 0


# Test the function
test_strings = [
    "",  # empty
    "()",  # simple
    "(){}[]",  # balanced multiple
    "([{}])",  # nested balanced
    "{[()]()}",  # balanced complex
    "([)]",  # incorrect nesting
    "((()))",  # deep nesting
    "(([]){}())",  # mixed
    "(",  # single opening
    ")",  # single closing
    "}{",  # wrong order
    "[({})](]",  # trailing mismatch
    "a(b)c",  # with other chars
    "{{{{",  # many opens
    "[]][",  # extra closings
    "[(])",
    "{(]}",
]
for test in test_strings:
    print(f"'{test}' is balanced: {is_balanced_parentheses(test)}")
