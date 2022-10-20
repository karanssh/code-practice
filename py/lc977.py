from typing import List 

def sortedSquares( nums: List[int]) -> List[int]:
    res = [0 ] * len(nums)
    # print(res)
    l = 0
    r = len(nums)-1 
    for i in range(len(nums)-1, -1,-1):
        if abs(nums[l])>abs(nums[r]):
            res[i] = nums[l]**2
            l+=1
        else:
            res[i] = nums[r]**2
            r-=1
    return res

if __name__ == '__main__':
    print(sortedSquares([-7,-3,2,3,11]))
    print(sortedSquares([-4,-1,0,3,10]))