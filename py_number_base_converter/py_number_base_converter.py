def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"

    try:
        base10_value = int(number, from_base)
    except ValueError:
        return "ERROR"

    if base10_value == 0:
        return "0"

    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while base10_value > 0:
        remainder = base10_value % to_base
        result += characters[remainder]
        base10_value //= to_base

    return result[::-1]


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))  # Output: "10"
    print(number_base_converter("FF", 16, 10))   # Output: "255"
    print(number_base_converter("255", 10, 16))  # Output: "FF"
    print(number_base_converter("123", 10, 2))   # Output: "1111011"
    print(number_base_converter("Z", 36, 10))    # Output: "35"
    print(number_base_converter("35", 10, 36))   # Output: "Z"
    print(number_base_converter("123", 1, 10))   # Output: "ERROR" (Base < 2)
    print(number_base_converter("G", 16, 10))    # Output: "ERROR" (G is not in Base 16)
