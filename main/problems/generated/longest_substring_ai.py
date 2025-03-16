def lengthOfLongestSubstring(s):
    char_index_map = {}
    longest_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        longest_length = max(longest_length, i - start + 1)

    return longest_length