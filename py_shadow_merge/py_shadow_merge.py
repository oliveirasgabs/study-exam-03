def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged_list = []
    i = 0  
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list


if __name__ == "__main__":
    print(shadow_merge([1, 3, 5], [2, 4, 6]))    # Output: [1, 2, 3, 4, 5, 6]
    print(shadow_merge([1, 2, 3], [4, 5, 6]))    # Output: [1, 2, 3, 4, 5, 6]
    print(shadow_merge([1], [2, 3, 4]))          # Output: [1, 2, 3, 4]
    print(shadow_merge([], [1, 2, 3]))           # Output: [1, 2, 3]
    print(shadow_merge([1, 1, 2], [1, 3, 3]))    # Output: [1, 1, 1, 2, 3, 3]