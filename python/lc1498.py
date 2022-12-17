from typing import List

def numSubseq(nums: List[int], target: int) -> int:
    nums.sort()
    res = 0
    mod = 10**9 + 7
    r = len(nums)-1
    for i, left in enumerate(nums):
        while (left + nums[r])> target and i <=r:
            r-=1
        if i<=r:
            res += pow(2, r - i, mod)
            res %= mod 
        
    return res


print(numSubseq([3,5,6,7], 9))