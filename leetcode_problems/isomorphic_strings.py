class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


s = "abab"
t = "baba"
print(Solution().isIsomorphic(s, t))
