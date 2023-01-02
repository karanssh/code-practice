from typing import List 

def findDisappearedNumbers(nums: List[int]) -> List[int]:
        d = set()
        for n in nums:
            d.add(n)
        res = []
        print(d)
        for i in range(1, len(nums)+1):
            if i not in d:
                res.append(i)
        print(res)
        return res


findDisappearedNumbers([4,3,2,7,8,2,3,1])