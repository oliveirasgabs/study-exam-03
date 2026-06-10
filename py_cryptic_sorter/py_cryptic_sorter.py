def cryptic_sorter(strings: list[str]) -> list[str]:
    def count_vowels(string: str) -> int:
        count: int = 0
        for c in string:
            if c in "aeiouAEIOU":
                count += 1
        return count

    def key_return(string: str):
        return (len(string), string.lower(), count_vowels(string))

    return sorted(strings, key=key_return)


if __name__ == "__main__":
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
    print(cryptic_sorter(["hello", "world", "hi", "test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))
