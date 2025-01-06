def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Replace negative numbers and zeros with n+1
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    
    # Step 2: Use the index as a hash map to record the presence of numbers
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first index with a positive value
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # If all indices are negative, the missing number is n + 1
    return n + 1