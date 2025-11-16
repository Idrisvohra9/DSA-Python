class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
