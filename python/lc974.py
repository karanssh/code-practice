class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = cur = 0
        prefix = {0:1} 
        for n in nums:
            cur += n
            mod = cur%k
            if mod<0:
                mod+=k
            
            res += prefix.get(mod, 0)
            prefix[mod] = prefix.get(mod,0) +1
        
        return res
