from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    def search(target, left):
        right = len(nums)-1
        while left < right:
            currSum = nums[left] + nums[right]
            if currSum == target:
                res.append([-target, nums[left], nums[right]])
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

    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        search(-nums[i], i+1)
    
    


    return res 

if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))