class MinStack:
    """
    Stack that can return minimum element in O(1) time.
    Uses auxiliary stack to track minimums.
    """

    # write your code in below funcs
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """Push element to stack. Time Complexity: O(1)"""
        self.stack.append(val)
        # If min_stack is empty OR val <= current min, push to min_stack too
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """Pop element from stack. Time Complexity: O(1)"""
        if not self.stack:
            return None
        removed = self.stack.pop()
        # If the removed element is the current minimum, pop from min_stack too (This makes sure that min_stack is synced with the stack)
        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        """Get minimum element. Time Complexity: O(1)"""
        return None if not self.stack else self.min_stack[-1]

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.stack) == 0


# Test the MinStack
min_stack = MinStack()
min_stack.push(5)
min_stack.push(2)
min_stack.push(8)
min_stack.push(1)

print(f"Minimum: {min_stack.get_min()}")  # Output: 1
min_stack.pop()
print(f"Minimum after pop: {min_stack.get_min()}")  # Output: 2
