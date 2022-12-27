from typing import List  


def findSubsetsWithDuplicates(nums):
    nums.sort()
    subsets = [[]]
    start, end = 0,0
    for i in range(len(nums)):
        start = 0 
        if i>0 and nums[i]==nums[i-1]:
            start = end+1 
        end = len(subsets)-1 
        for j in range(start, end+1):
            s = subsets[j].copy()
            s.append(nums[i])
            subsets.append(s)
    # print(subsets)
    return subsets 

findSubsetsWithDuplicates([1,2,2,3])

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return

        # All subsets that include nums[i]
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        # All subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res
    