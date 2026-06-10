def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k = k % len(arr)
    if k == 0:
        return arr
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3]
    print(twist_sequence([1, 2, 3], 1))       # Output: [3, 1, 2]
    print(twist_sequence([1, 2, 3, 4], 0))    # Output: [1, 2, 3, 4]
    print(twist_sequence([1, 2, 3], 5))       # Output: [2, 3, 1]
    print(twist_sequence([], 3))              # Output: []