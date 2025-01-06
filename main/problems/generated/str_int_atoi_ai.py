def myAtoi(s):
    # Define the 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Initialize variables
    index = 0
    sign = 1
    total = 0
    n = len(s)

    # Discard leading whitespaces
    while index < n and s[index] == ' ':
        index += 1

    # Check for optional sign
    if index < n and (s[index] == '+' or s[index] == '-'):
        sign = -1 if s[index] == '-' else 1
        index += 1

    # Convert digits to integer
    while index < n and s[index].isdigit():
        digit = int(s[index])
        
        # Check for overflow and clamp the value
        if total > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        total = total * 10 + digit
        index += 1

    return sign * total