def bracket_validator(s: str) -> bool:
    for letter in s:
        if (letter not in "[{()}]"):
            s = s.replace(letter, "")
    for key in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    if s == "":
        return True
    else:
        return False


if __name__ == "__main__":
    print(bracket_validator("()"))                       # Output: True
    print(bracket_validator("()[]{}"))                   # Output: True
    print(bracket_validator("(]"))                       # Output: False
    print(bracket_validator("([)]"))                     # Output: False
    print(bracket_validator("{[]}"))                     # Output: True
    print(bracket_validator("hello(world)[test]{code}")) # Output: True
    print(bracket_validator("((()))"))                   # Output: True
    print(bracket_validator("((())"))                    # Output: False
    print(bracket_validator(""))                         # Output: True
