from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return [
            ch
            for ch in set(words[0])
            for _ in range(min(word.count(ch) for word in words))
        ]


words = ["bella", "label", "roller"]
print(Solution().commonChars(words))
