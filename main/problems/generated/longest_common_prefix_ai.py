def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the string
        while not string.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last character from prefix
            if not prefix:
                return ""
    
    return prefix