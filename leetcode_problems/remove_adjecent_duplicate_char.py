class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            # If stack is not empty and top element equals current char
            if stack and stack[-1] == char:
                stack.pop()  # Remove the duplicate pair
            else:
                stack.append(char)  # Add char to stack

        return "".join(stack)


print(Solution().removeDuplicates("abbaca"))
