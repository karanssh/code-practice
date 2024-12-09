from typing import List


def sortedSquaresNaive(nums: List[int]) -> List[int]:

    nums = [x**2 for x in nums]
    return sorted(nums)

def sortedSquares(nums: List[int]) -> List[int]:

    l = 0
    r = len(nums)-1
    res = [0]* len(nums)
    idx = r
    while l<r:
        if nums[l]**2 < nums[r]**2:
            res[idx] = nums[r]**2
            r-=1
        else:
            res[idx] = nums[l]**2
            l+=1
        idx-=1

    return res


if __name__ == "__main__":
    print(sortedSquaresNaive([-2,-1,0,2,3]))
    print(sortedSquares([-2,-1,0,2,3]))
