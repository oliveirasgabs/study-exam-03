def string_sculptor(text: str) -> str:
    position: int = 0
    result = []
    for c in text:
        if c.isalpha():
            if ((position % 2) == 0) and c.islower():
                result.append(c.upper())
            elif (position % 2 >= 1) and c.isupper():
                result.append(c.lower())
            else:
                result.append(c)
        else:
            result.append(c)
        position += 1
    
    return "".join(result)


if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("aBc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))