def zigzag_conversion(s, num_rows):
    if num_rows <= 1 or num_rows >= len(s):
        return s

    rows = [""] * num_rows
    go_down = True
    row_num = 0
    for char in s:
        rows[row_num] += char

        if row_num >= num_rows - 1:
            go_down = False
        elif row_num == 0:
            go_down = True
        row_num += 1 if go_down else -1
    return "".join(rows)

print(zigzag_conversion("PAYPALISHIRING", 5))