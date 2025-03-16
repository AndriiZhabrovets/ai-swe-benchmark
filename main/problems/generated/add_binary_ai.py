
def addBinary(a, b):
    
    return 








def add_bin(a, b):
    # Initialize pointers for both strings starting from the end
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    # Loop until both strings are processed or carry is still present
    while i >= 0 or j >= 0 or carry:
        # Get the current bits and add them along with the carry
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        
        total = bit_a + bit_b + carry
        
        # Compute the new bit and the new carry
        result.append(str(total % 2))  # Add the result bit (0 or 1)
        carry = total // 2              # Update carry (0 or 1)

        # Move to the next bits
        i -= 1
        j -= 1
    
    # The result is in reverse order, reverse it back
    return ''.join(reversed(result))
