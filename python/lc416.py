from typing import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True  # base case: 0 sum is always achievable (empty subset)

    for num in nums:
        # iterate backwards to prevent using the same number multiple times
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]

    return dp[target]



# Example usage:
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True