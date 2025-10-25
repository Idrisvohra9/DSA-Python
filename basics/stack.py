class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            # Gets the last item without removing it
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.items)
    
    # We are defining the string representation of the stack for easy visualization
    def __str__(self):
        return str(self.items)
    
# Example usage:
# If this is the main file that is being run then execute the following code
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print("Stack after pushes:", stack)  # Output: [1, 2, 3]
    print("Top item:", stack.peek())      # Output: 3
    print("Popped item:", stack.pop())     # Output: 3
    print("Stack after pop:", stack)       # Output: [1, 2]
    print("Is empty?", stack.is_empty())   # Output: False
    print("Stack size:", stack.size())     # Output: 2