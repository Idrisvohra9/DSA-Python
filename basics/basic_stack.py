# Creating an empty stack using list
stack = []

# Push items into the stack using .append()
stack.append(1)
stack.append(2)
stack.append(3)

# Peek at the top item:
print("Top item:", stack[-1])  # Output: 3

# Pop items from the stack using .pop()
print("Popped:", stack.pop())  # Output: 3, Stack: [1,2]
print("Popped:", stack.pop())  # Output: 2, Stack: [3]

# Check if stack is empty or not (returns bool)
print("Is empty?", len(stack) == 0)  # Output: False
