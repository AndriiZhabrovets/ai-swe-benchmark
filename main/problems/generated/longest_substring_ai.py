def lengthOfLongestSubstring(s):
    char_index_map = {}
    longest = 0
    start = 0

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = index
        longest = max(longest, index - start + 1)

    return longest