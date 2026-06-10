def whisper_cipher(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)
    return "".join(result)


f __name__ == "__main__":
    print(whisper_cipher("hello", 3))         # Output: "khoor"
    print(whisper_cipher("Hello World!", 1))  # Output: "Ifmmp Xpsme!"
    print(whisper_cipher("xyz", 3))           # Output: "abc"
    print(whisper_cipher("ABC123def", 5))     # Output: "FGH123ijk"
    print(whisper_cipher("", 10))             # Output: ""