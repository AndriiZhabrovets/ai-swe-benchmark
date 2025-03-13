def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Initialize the prefix as the first string
    prefix = strs[0]
    
    for string in strs[1:]:
        # Compare the current string with the prefix
        while string[:len(prefix)] != prefix and prefix:
            # Reduce the prefix by one character from the end
            prefix = prefix[:-1]
        
        # If prefix becomes empty, no common prefix exists
        if not prefix:
            break
            
    return prefix