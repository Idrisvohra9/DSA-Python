"""
STACK PROBLEMS & SOLUTIONS
==========================
Collection of well-known stack problems with optimal solutions.
Stack follows LIFO (Last In, First Out) principle - perfect for problems involving
nested structures, backtracking, and expression evaluation.
"""

# ============================================================================
# PROBLEM 1: VALID PARENTHESES
# ============================================================================
def is_valid_parentheses(s):
    """
    Problem: Check if string of parentheses is valid.
    Valid means: (), [], {} are properly opened and closed.
    
    Approach: Use stack to match opening and closing brackets
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "()[]{}" → True, "([)]" → False
    """
    # Stack to store opening brackets
    stack = []
    
    # Mapping of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening bracket
            stack.append(char)
    
    # Valid if all brackets are matched (stack is empty)
    return not stack

# ============================================================================
# PROBLEM 2: EVALUATE REVERSE POLISH NOTATION (RPN)
# ============================================================================
def eval_rpn(tokens):
    """
    Problem: Evaluate arithmetic expression in Reverse Polish Notation.
    
    Approach: Use stack to store operands, apply operators when encountered
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: ["2","1","+","3","*"] → ((2 + 1) * 3) = 9
    """
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            # Pop two operands (note the order!)
            b = stack.pop()
            a = stack.pop()
            
            # Apply operation
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # token == '/'
                # Integer division towards zero
                result = int(a / b)
            
            stack.append(result)
        else:
            # Push operand to stack
            stack.append(int(token))
    
    # Final result
    return stack[0]

# ============================================================================
# PROBLEM 3: DAILY TEMPERATURES
# ============================================================================
def daily_temperatures(temperatures):
    """
    Problem: Find how many days you have to wait for warmer temperature.
    
    Approach: Monotonic decreasing stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
    """
    result = [0] * len(temperatures)
    stack = []  # Store indices
    
    for i, temp in enumerate(temperatures):
        # While stack not empty and current temp > temp at stack top
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        
        stack.append(i)
    
    return result

# ============================================================================
# PROBLEM 4: LARGEST RECTANGLE IN HISTOGRAM
# ============================================================================
def largest_rectangle_area(heights):
    """
    Problem: Find area of largest rectangle in histogram.
    
    Approach: Monotonic increasing stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Logic: For each bar, find the largest rectangle with that bar as the shortest bar.
    """
    stack = []  # Store indices
    max_area = 0
    
    for i, height in enumerate(heights):
        # While current height < height at stack top
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            # Width is current index - previous index in stack - 1
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        stack.append(i)
    
    # Process remaining bars in stack
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

# ============================================================================
# PROBLEM 5: MIN STACK
# ============================================================================
class MinStack:
    """
    Problem: Design stack that supports push, pop, top, and getMin in O(1).
    
    Approach: Use auxiliary stack to track minimums
    Space Complexity: O(n)
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Keeps track of minimums
    
    def push(self, val):
        """Push element onto stack. O(1)"""
        self.stack.append(val)
        # Push to min_stack if it's empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        """Remove top element. O(1)"""
        if self.stack:
            val = self.stack.pop()
            # If popped value was minimum, remove from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        """Get top element. O(1)"""
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        """Get minimum element. O(1)"""
        return self.min_stack[-1] if self.min_stack else None

# ============================================================================
# PROBLEM 6: IMPLEMENT QUEUE USING STACKS
# ============================================================================
class MyQueue:
    """
    Problem: Implement queue using only stacks.
    
    Approach: Use two stacks - one for enqueue, one for dequeue
    Amortized Time Complexity: O(1) for all operations
    """
    
    def __init__(self):
        self.input_stack = []   # For enqueue operations
        self.output_stack = []  # For dequeue operations
    
    def push(self, x):
        """Add element to back of queue."""
        self.input_stack.append(x)
    
    def pop(self):
        """Remove element from front of queue."""
        self.peek()  # Ensure output_stack has elements
        return self.output_stack.pop()
    
    def peek(self):
        """Get front element without removing."""
        if not self.output_stack:
            # Transfer all elements from input to output
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]
    
    def empty(self):
        """Check if queue is empty."""
        return not self.input_stack and not self.output_stack

# ============================================================================
# PROBLEM 7: NEXT GREATER ELEMENT
# ============================================================================
def next_greater_element(nums1, nums2):
    """
    Problem: Find next greater element for each element in nums1 within nums2.
    
    Approach: Monotonic decreasing stack + hash map
    Time Complexity: O(n + m)
    Space Complexity: O(n)
    
    Example: nums1=[4,1,2], nums2=[1,3,4,2] → [-1,3,-1]
    """
    # Build next greater element mapping for nums2
    next_greater = {}
    stack = []
    
    for num in nums2:
        # While stack not empty and current > stack top
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    # For remaining elements in stack, no greater element exists
    while stack:
        next_greater[stack.pop()] = -1
    
    # Build result for nums1
    return [next_greater[num] for num in nums1]

# ============================================================================
# PROBLEM 8: SIMPLIFY PATH
# ============================================================================
def simplify_path(path):
    """
    Problem: Simplify Unix-style file path.
    
    Approach: Use stack to process path components
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "/a/./b/../../c/" → "/c"
    """
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '..' and stack:
            stack.pop()  # Go to parent directory
        elif component and component != '.' and component != '..':
            stack.append(component)  # Valid directory name
        # Ignore empty strings and '.'
    
    return '/' + '/'.join(stack)

# ============================================================================
# PROBLEM 9: DECODE STRING
# ============================================================================
def decode_string(s):
    """
    Problem: Decode string with pattern k[encoded_string].
    
    Approach: Use stack to handle nested patterns
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "3[a2[c]]" → "accaccacc"
    """
    stack = []
    current_num = 0
    current_string = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current state to stack
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop and decode
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char
    
    return current_string

# ============================================================================
# PROBLEM 10: BASIC CALCULATOR
# ============================================================================
def calculate(s):
    """
    Problem: Evaluate basic mathematical expression with +, -, (, ).
    
    Approach: Use stack to handle parentheses
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "(1+(4+5+2)-3)+(6+8)" → 23
    """
    stack = []
    result = 0
    number = 0
    sign = 1  # 1 for +, -1 for -
    
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == '+':
            result += sign * number
            number = 0
            sign = 1
        elif char == '-':
            result += sign * number
            number = 0
            sign = -1
        elif char == '(':
            # Push current result and sign to stack
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            # Complete current calculation
            result += sign * number
            number = 0
            # Pop sign and previous result
            result *= stack.pop()  # sign
            result += stack.pop()  # previous result
    
    return result + sign * number

# ============================================================================
# PROBLEM 11: ASTEROID COLLISION
# ============================================================================
def asteroid_collision(asteroids):
    """
    Problem: Simulate asteroid collisions. Positive = right, negative = left.
    
    Approach: Use stack to track surviving asteroids
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: [5,10,-5] → [5,10] (10 and -5 collide, 10 survives)
    """
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            # Collision: right-moving meets left-moving
            if stack[-1] < -asteroid:
                stack.pop()  # Right-moving asteroid explodes
                continue
            elif stack[-1] == -asteroid:
                stack.pop()  # Both explode
            break  # Left-moving asteroid explodes or both explode
        else:
            stack.append(asteroid)  # No collision
    
    return stack

# ============================================================================
# PROBLEM 12: REMOVE K DIGITS
# ============================================================================
def remove_k_digits(num, k):
    """
    Problem: Remove k digits from number to make it smallest possible.
    
    Approach: Monotonic increasing stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: num="1432219", k=3 → "1219"
    """
    stack = []
    to_remove = k
    
    for digit in num:
        # Remove larger digits from stack
        while stack and to_remove > 0 and stack[-1] > digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    # Remove remaining digits from end if needed
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    # Convert to string and handle edge cases
    result = ''.join(stack).lstrip('0')
    return result if result else '0'

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def test_stack_problems():
    """Test all stack problems with examples."""
    
    print("=== STACK PROBLEMS & SOLUTIONS ===\n")
    
    # Test 1: Valid Parentheses
    print("1. VALID PARENTHESES")
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for case in test_cases:
        print(f"'{case}' → {is_valid_parentheses(case)}")
    
    # Test 2: Evaluate RPN
    print("\n2. EVALUATE RPN")
    rpn_tokens = ["2", "1", "+", "3", "*"]
    print(f"{rpn_tokens} → {eval_rpn(rpn_tokens)}")
    
    # Test 3: Daily Temperatures
    print("\n3. DAILY TEMPERATURES")
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Temperatures: {temps}")
    print(f"Days to wait: {daily_temperatures(temps)}")
    
    # Test 4: Largest Rectangle
    print("\n4. LARGEST RECTANGLE IN HISTOGRAM")
    heights = [2, 1, 5, 6, 2, 3]
    print(f"Heights: {heights}")
    print(f"Largest area: {largest_rectangle_area(heights)}")
    
    # Test 5: Min Stack
    print("\n5. MIN STACK")
    min_stack = MinStack()
    operations = [
        ("push", -2), ("push", 0), ("push", -3),
        ("getMin", None), ("pop", None), ("top", None), ("getMin", None)
    ]
    for op, val in operations:
        if op == "push":
            min_stack.push(val)
            print(f"Push {val}")
        elif op == "pop":
            min_stack.pop()
            print("Pop")
        elif op == "top":
            print(f"Top: {min_stack.top()}")
        elif op == "getMin":
            print(f"Min: {min_stack.get_min()}")
    
    # Test 6: Next Greater Element
    print("\n6. NEXT GREATER ELEMENT")
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(f"nums1: {nums1}, nums2: {nums2}")
    print(f"Next greater: {next_greater_element(nums1, nums2)}")
    
    # Test 7: Simplify Path
    print("\n7. SIMPLIFY PATH")
    paths = ["/home/", "/../", "/home//foo/", "/a/./b/../../c/"]
    for path in paths:
        print(f"'{path}' → '{simplify_path(path)}'")
    
    # Test 8: Decode String
    print("\n8. DECODE STRING")
    encoded = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    for s in encoded:
        print(f"'{s}' → '{decode_string(s)}'")

if __name__ == "__main__":
    test_stack_problems()