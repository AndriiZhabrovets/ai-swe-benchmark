def myAtoi(s):
    s = s.lstrip()  # Remove leading whitespace
    if not s:
        return 0
    
    sign = 1
    index = 0
    n = len(s)
    
    # Check for sign
    if s[index] == '+':
        index += 1
    elif s[index] == '-':
        sign = -1
        index += 1
    
    result = 0
    
    # Process digits
    while index < n and s[index].isdigit():
        digit = int(s[index])
        # Check for overflow
        if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
            return 2**31 - 1 if sign == 1 else -2**31
        result = result * 10 + digit
        index += 1
    
    return sign * result