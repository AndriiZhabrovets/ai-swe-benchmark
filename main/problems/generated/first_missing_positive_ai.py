def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Remove negative numbers and numbers larger than n
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1  # Replace with a number out of the range of interest

    # Step 2: Use the index as a hash key and mark the numbers present
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])  # Mark as negative to indicate presence

    # Step 3: Find the first index which is not negative
    for i in range(n):
        if nums[i] > 0:
            return i + 1  # The first missing positive is i + 1

    return n + 1  # If all numbers from 1 to n are present, return n + 1