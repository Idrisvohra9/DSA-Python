from typing import List


# def strStr(haystack: str, needle: str) -> int:
#     if not needle in haystack:
#         return -1
#     for i in range(len(haystack), 0, -1):
#         if haystack[i - len(needle) : i] == needle:
#             return i - len(needle)
#     return -1
#     return haystack.find(needle)


def strStr(haystack: str, needle: str) -> int:
    if not needle in haystack:
        return -1

    for i in range(len(haystack)):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))
