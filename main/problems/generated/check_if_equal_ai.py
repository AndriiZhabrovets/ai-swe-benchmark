def hasSameDigits(s):
    while len(s) > 2:
        new_s = []
        for i in range(len(s) - 1):
            new_digit = (int(s[i]) + int(s[i + 1])) % 10
            new_s.append(str(new_digit))
        s = ''.join(new_s)
    return s[0] == s[1]