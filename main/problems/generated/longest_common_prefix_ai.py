def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the string
        while not string.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last character of the prefix
            if not prefix:  # If prefix becomes empty, return ""
                return ""
    
    return prefix