from functools import lru_cache
from typing import List
# Given a list of integers and a target integer, this function returns the number of ways to assign
# symbols to make the sum of the integers equal to the target integer.
# The symbols can be either '+' or '-'.
# The function uses memoization to optimize the recursive calls.
# The function is defined within a class named Solution.
# The function takes two parameters: nums (a list of integers) and target (an integer).
# The function uses a helper function dfs (depth-first search) to explore all possible combinations of
# assigning symbols to the integers in the list.
# The dfs function takes two parameters: i (the current index in the nums list) and t (the current sum).
# The dfs function checks if the current index i is equal to the length of the nums list.
# If it is, it checks if the current sum t is equal to the target integer.
# If it is, it returns 1 (indicating one valid way to assign symbols).
# If not, it returns 0 (indicating no valid way).
# If the current index i is not equal to the length of the nums list, the dfs function recursively calls
# itself twice: once with the current integer added to the sum (t + nums[i]) and once with the current
# integer subtracted from the sum (t - nums[i]).
# The results of these two recursive calls are added together to get the total number of ways to assign
# symbols for the current index i.
# The dfs function is decorated with lru_cache to cache the results of previous calls, which helps
# optimize the performance of the function by avoiding redundant calculations.
# The main function returns the result of the dfs function starting from index 0 and an initial sum of 0.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, t):
            if i == len(nums):
                return 1 if t == target else 0
            return dfs(i+1, t+nums[i]) + dfs(i+1, t-nums[i])

        return dfs(0, 0)
