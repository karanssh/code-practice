from typing import List

def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True  # base case

    for i in range(1, n + 1):
        for t in range(1, target + 1):
            if nums[i - 1] > t:
                dp[i][t] = dp[i - 1][t]
            else:
                dp[i][t] = dp[i - 1][t] or dp[i - 1][t - nums[i - 1]]

    return dp[n][target]


# Example usage:
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True