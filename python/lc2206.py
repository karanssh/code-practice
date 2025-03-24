from typing import Counter, List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        c = Counter(nums)
        for n in c:
            if c[n]%2!=0:
                return False
        
        return True