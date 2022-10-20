from typing import List 

def searchInsert( nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    res = 0
    while l<=r:
        mid = (l+r) // 2 
        if nums[mid] == target:
            return mid
        # if mid - 1 > 0 and mid +1< len(nums)-1 and nums[mid+1]>target and nums[mid-1]<target:
        #     res = mid
        if nums[mid]<target:
            l = mid +1
        if nums[mid]>target:
            r = mid - 1
    # print(res)
    # print(mid)
    if nums[mid] > target:
        return mid
    else:
        return mid + 1


print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))