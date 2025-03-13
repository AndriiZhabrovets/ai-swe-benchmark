def firstMissingPositive(nums):
    n = len(nums)
    
    # First, we replace all numbers that are not in the range [1, n] with a placeholder (n + 1)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
            
    # Use the index to mark the presence of numbers in the array
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Now, the first index that has a positive value is our answer
    for i in range(n):
        if nums[i] > 0:
            return i + 1
            
    # If all indices are marked, the missing positive is n + 1
    return n + 1