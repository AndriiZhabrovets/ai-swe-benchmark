Here’s a Python function to add two binary numbers represented as strings:

```python
def add_binary(a: str, b: str) -> str:
    """Adds two binary numbers represented as strings and returns the sum as a binary string."""
    return bin(int(a, 2) + int(b, 2))[2:]

# Example usage
binary1 = "1011"
binary2 = "1101"
result = add_binary(binary1, binary2)
print(f"{binary1} + {binary2} = {result}")

```

### Explanation:
	1.	int(a, 2): Converts the binary string a to an integer.
	2.	int(b, 2): Converts the binary string b to an integer.
	3.	int(a, 2) + int(b, 2): Adds the two integers.
	4.	bin(...)[2:]: Converts the sum back to a binary string and removes the "0b" prefix.

This is a clean and efficient approach using Python’s built-in functions.