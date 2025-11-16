class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(ch) for ch in str(int("".join(map(str, digits))) + 1)]

        
digits = [9]
print(Solution().plusOne(digits))