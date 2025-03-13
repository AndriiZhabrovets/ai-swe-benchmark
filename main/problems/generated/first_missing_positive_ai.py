def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Replace negative numbers and zeros with a number larger than n
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
            
    # Step 2: Use the index as a hash to mark the presence of numbers
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first index that has a positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1
            
    # Step 4: If all indices are negative, return n + 1
    return n + 1