def myAtoi(s):
    s = s.lstrip()  # Remove leading whitespace
    if not s:
        return 0
    
    sign = 1
    index = 0
    result = 0
    max_int = 2**31 - 1
    min_int = -2**31
    
    # Check for optional sign
    if s[index] == '+' or s[index] == '-':
        sign = 1 if s[index] == '+' else -1
        index += 1
    
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        
        # Check for overflow and underflow
        if (result > max_int // 10) or (result == max_int // 10 and digit > 7):
            return max_int if sign == 1 else min_int
        
        result = result * 10 + digit
        index += 1
    
    return result * sign