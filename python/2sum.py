from typing import List

def twoSumSorted(nums: List[int], target: int) -> List[List[int]]:

    res = []
    nums.sort()
    left = 0
    right = len(nums)-1
    while left < right:
        currSum = nums[left] + nums[right]
        if currSum == target:
            res.append([nums[left], nums[right]])
            left +=1
            right-=1
            while(left<right and nums[left]==nums[left-1]):
                left +=1
            while(left<right and nums[right]==nums[right+1]):
                right -=1
        elif target>currSum:
            left +=1
        else:
            right-=1

    return res 

# return all possible variations
def twoSumMap(nums: List[int], target: int) -> List[List[int]]:
    res = []
    mp = set() # using a hashSet
    for i in range(len(nums)):
        if target-nums[i] in mp:
            res.append([nums[i], (target-nums[i])])
        mp.add(nums[i])
    return res


if __name__ == "__main__":
    print(twoSumSorted([-1,0,1,2,-1,-4], 0))
    print(twoSumMap([-1,0,1,2,-1,-4], 0))