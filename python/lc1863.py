from typing import List 

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_total(arr):
            res = 0
            for a in arr:
                res ^= a

            return res
        
        n = len(nums)
        subsets = []
        def dfs(i, path):
            if i == n:
                subsets.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        
        answer = 0 
        for el in subsets:
            answer += xor_total(el)
        
        return answer