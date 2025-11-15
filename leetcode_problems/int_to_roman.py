def intToRoman(num: int) -> str:
    """Convert 1 <= num <= 3999 to Roman numerals."""
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    parts = []

    for v, s in zip(vals, syms):
        if count := num // v:
            parts.append(s * count)
            num -= v * count
        if num == 0:
            break
    return "".join(parts)

# Example:
print(intToRoman(1994))  # MCMXCIV

# def intToRoman(num):
#     roman_map = {
#         1000: "M", 900: "CM",
#         500: "D", 400: "CD",
#         100: "C", 90: "XC",
#         50: "L", 40: "XL",
#         10: "X", 9: "IX",
#         5: "V", 4: "IV",
#         1: "I"
#     }
 
#     result = ""
#     for value in roman_map:
#         while num >= value:
#             result += roman_map[value]
#             num -= value
#     return result