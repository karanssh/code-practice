from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for a in range(len(nums)):
        if nums[a] != val:
            nums[i] = nums[a]
            i +=1 

    return i