def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Replace non-positive numbers and numbers larger than n with n+1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
            
    # Step 2: Use the index as a hash to mark the presence of numbers
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1
            
    return n + 1