def atoai(s=""):
    if not s:
        return 0
    s = s.lstrip(" ")
    if not s:
        return 0
    # Early exit: if first char is not digit or sign
    if not (s[0].isdigit() or s[0] == '+' or s[0] == '-'):
        return 0
    is_negative = False
    if s[0] == '+' or s[0] == '-':
        if len(s) > 1 and (s[1] == '+' or s[1] == '-'):
            return 0  # Multiple signs, invalid
        if s[0] == '-':
            is_negative = True
        s = s[1:]
    # Use list to collect digits
    digits = []
    for char in s:
        if char.isdigit():
            digits.append(char)
        else:
            break
    if not digits:
        return 0
    num = ''.join(digits)
    val = int(num)
    if is_negative:
        val = -val
    # 32 bit signed integer limits
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    if val < INT_MIN:
        return INT_MIN
    if val > INT_MAX:
        return INT_MAX
    return val


print(atoai("1337c0d3"))
