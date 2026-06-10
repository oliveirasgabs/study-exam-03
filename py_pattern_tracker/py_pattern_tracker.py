def pattern_tracker(text: str) -> int:
    count = 0

    for i in range(len(text) - 1):
        current_char = text[i]
        next_char = text[i + 1]

        if current_char.isdigit() and next_char.isdigit():
            if int(next_char) == int(current_char) + 1:
                count += 1

    return count


if __name__ == "__main__":
    print(pattern_tracker("123"))       # Output: 2
    print(pattern_tracker("12a34"))     # Output: 2
    print(pattern_tracker("987654321")) # Output: 0
    print(pattern_tracker("01234567"))  # Output: 7
    print(pattern_tracker("abc"))       # Output: 0
    print(pattern_tracker("1a2b3c4"))   # Output: 0
    print(pattern_tracker("112233"))    # Output: 2
