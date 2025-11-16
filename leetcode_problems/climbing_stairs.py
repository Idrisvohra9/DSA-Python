class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a, b = 1, 2  # a = F(0), b = F(1)
        for _ in range(2, n):
            a, b = b, a + b  # move the window forward
        return b
    
print(Solution().climbStairs(6))