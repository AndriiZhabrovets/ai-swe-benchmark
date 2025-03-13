def longestPalindrome(s):
    if not s:
        return ""

    start, end = 0, 0

    def expand_around_center(left, right):
        nonlocal start, end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > end - start:
            start = left + 1
            end = right - 1

    for i in range(len(s)):
        expand_around_center(i, i)     # Odd length palindromes
        expand_around_center(i, i + 1) # Even length palindromes

    return s[start:end + 1]