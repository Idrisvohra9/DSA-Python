import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return math.isqrt(x)
    
x = 4
print(Solution().mySqrt(x))