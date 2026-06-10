def echo_validator(text: str) -> bool:
    cleaned_text = ""
    for char in text:
        if char.isalpha():
            cleaned_text += char.lower()
    if cleaned_text == "":
        return False
    
    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    print(echo_validator("racecar"))                     # Output: True
    print(echo_validator("A man a plan a canal Panama")) # Output: True
    print(echo_validator("race a car"))                  # Output: False
    print(echo_validator("Was it a car or a cat I saw")) # Output: True
    print(echo_validator("hello"))                       # Output: False
    print(echo_validator("Madam Im Adam"))               # Output: True
    print(echo_validator(""))                            # Output: False