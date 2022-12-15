from typing import List 

def minimumDifference(nums: List[int], k: int) -> int:
        if len(nums) <=1:
            return 0
        nums.sort()
        res = float("inf")
        j = 0
        for i in range(1, len(nums)):
            if i >= k-1:
                res = min(res, (nums[i]-nums[j]))
                j+=1
        return res

if __name__ == "__main__":
    print(minimumDifference([9,4,1,7], 2))
