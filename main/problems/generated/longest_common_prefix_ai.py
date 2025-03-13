def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start by assuming the whole first string is the common prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for s in strs[1:]:
        # Reduce the prefix until it matches the start of the string s
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last character
            if not prefix:  # If prefix is empty, return immediately
                return ""
    
    return prefix