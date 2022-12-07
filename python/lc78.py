from typing import List 

def subsets(nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            # copy and pick 
            r = len(res)
            for i in range(r):
                s = res[i].copy()
                s.append(n)
                res.append(s)
        return res 

print(subsets([1,2,3]))