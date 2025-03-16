def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the prefix as the first string
    prefix = strs[0]
    
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the string
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        
        if not prefix:
            break
    
    return prefix