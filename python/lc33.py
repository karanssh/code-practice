from typing import List 

def searchInRotatedSortedArray(nums: List[int], target: int) -> int:
    l = 0 
    r = len(nums)-1
    while l<=r:
        mid = (l+r) // 2 
        if nums[mid] == target:
            return mid 
        
        if nums[mid] >= nums[l]:
            if target<nums[l] or target > nums[mid]:
                l = mid +1 
            else:
                r = mid -1 
        else:
            if target <nums[mid] or target >nums[r]:
                r = mid -1
            else:
                l = mid +1  
    return -1 


print(
    searchInRotatedSortedArray([4,5,6,7,0,1,2], 0)
    )
