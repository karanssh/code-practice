from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    res = 0
    n = len(cost)
    dp = [0 for i in range(n)] 
   

    def minCost(cost, n, dp):
        if n<0:
            return 
        if n == 0 or n == 1:
            return cost[n]
        if dp[n]!=0:
            return dp[n]
        dp[n] = cost[n]+ min(minCost(cost, n-1, dp), minCost(cost, n-2, dp))
        return dp[n]

    res = min(minCost(cost, n-1, dp), minCost(cost, n-2, dp))
    return res 

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))