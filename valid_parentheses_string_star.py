def checkValidString(s: str) -> bool:
    # Stack to store indices of opening parentheses
    open_stack = []
    # Stack to store indices of stars
    star_stack = []

    # First pass: process each character
    for i, ch in enumerate(s):
        if ch == "(":
            open_stack.append(i)
        elif ch == "*":
            star_stack.append(i)
        else:  # ch == ')'
            # Try to match with an opening parenthesis first
            if open_stack:
                open_stack.pop()
            # If no opening parenthesis, try to match with a star
            elif star_stack:
                star_stack.pop()
            # If neither available, invalid
            else:
                return False
    # print("Open Stack", open_stack)
    # print("Star Stack", star_stack)

    # Second pass: match remaining opening parentheses with stars
    while open_stack and star_stack:
        # Get the position of the last unmatched opening parenthesis
        open_pos = open_stack.pop()
        # Get the position of the last available star
        star_pos = star_stack.pop()
        # print("Open parentheses position:", open_pos)
        # print("Star position:", star_pos)

        # Star can only close an opening parenthesis if it comes after it
        if star_pos < open_pos:
            return False
    # Valid if all opening parentheses are matched
    return len(open_stack) == 0


test_cases = [
    # "*",
    "(**(*()**()**((**(*)",
    # "((*)(*))()*(*)****((*(*)())*()((()**(**)",
    # ")(*()(**(*)())*))())())*)()()*(((*)()))(**()*)**(*",
    # ")))(*)**)))*)))))*)*(((()(((*())(***)**(**((()))()((*((()(((",
    # "()))))**)(()*()**)))()*)()())*(*)())**()*)))(**())))()**))*)*()**((*(*",
    # "*(*)(*))((*)*)))(*)())*())()(()*)*)****)())(()()*(*(*())()((())))*()****)(*(()))((*()*(**(*()*)*()",
    # "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())",
]
for case in test_cases:
    print(f"Is this {case} Valid parentheses?", checkValidString(case))
