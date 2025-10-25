def second_largest_digit(s: str) -> int:
    digits = []
    for ch in s:
        if ch.isdigit():
            digits.append(int(ch))
    a = sorted(set(digits))
    if len(a) > 1:
        return a[-2]
    return -1

stringExample = "13abc13b4"
print("Second largest digit in a string", second_largest_digit(stringExample))