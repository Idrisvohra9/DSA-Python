def remove_spaces(s: str) -> str:
    arr = []
    for ch in s:
        if ch != " ":
            arr.append(ch)
    return "".join(arr)
    # return s.replace(" ", "")


print(remove_spaces("Hi John"))
