from typing import List 

def canJump(nums: List[int]) -> bool:
        
        dp = [0] * len(nums)
        dp[0] = True
        
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and nums[j] >= (i-j):
                    dp[i] = True
                    break
        return dp[-1]

def canJump2(nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


print( 
    canJump(
        [2,3,1,1,4]
    )
)