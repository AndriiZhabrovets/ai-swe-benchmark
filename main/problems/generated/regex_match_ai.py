def isMatch(s, p):
    # Create a DP table with dimensions (len(s)+1) x (len(p)+1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty string and empty pattern match
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, a*b*c* that can match empty string
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Treat '*' as matching zero occurrences
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # Treat '*' as matching one or more occurrences
    
    return dp[len(s)][len(p)]