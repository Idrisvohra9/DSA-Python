class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.square(n)
        return n == 1

    def square(self, n):
        sum = 0
        while n != 0:
            sum += (n % 10) * (n % 10)
            n = n // 10
        return sum


print(Solution().isHappy(19))
