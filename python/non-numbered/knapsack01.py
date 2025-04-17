from typing import List

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    # Create dp table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]  # can't include item
            else:
                dp[i][w] = max(dp[i - 1][w], 
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    return dp[n][capacity]
# Example usage:

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
print(knapsack_01(weights, values, capacity))  # Output: 65