from typing import List 

# longest substring with K unique characters

def substringWithKUniqueCharacters(s: str, k: int):
    windowStart = 0
    mp = {}
    res = ""
    maxLen = 0
    for windowEnd in range(len(s)):
        mp[s[windowEnd]] = 1+ mp.get(s[windowEnd], 0)

        while len(mp.keys())>k:
            mp[s[windowStart]] -=1
            if mp[s[windowStart]] == 0:
                del mp[s[windowStart]]
            windowStart +=1
        if windowEnd-windowStart+1 > maxLen:
            res = s[windowStart:windowEnd+1]
        maxLen = max(maxLen, windowEnd-windowStart+1)
    print(res)
    return maxLen

def runsmallestSubarraySumGreatherEqualK():
    print(substringWithKUniqueCharacters("araaci", 2))

# smallest subarray with a sum >=K

def smallestSubarraySumGreatherEqualK(nums: List[int], k: int) -> List[int]:
    windowStart = 0
    windowEnd = 0
    res = []
    sM = float("-inf")
    resLen = float("inf")
    while windowEnd <len(nums):
        subarray = nums[windowStart:windowEnd+1]
        if sum(subarray)>=k:
            sM = max(sM, sum(subarray))
            if len(subarray)<resLen:
                resLen = len(subarray)
                res = subarray
            windowStart+=1
        else:
            windowEnd+=1

    return res 

def runsmallestSubarraySumGreatherEqualK():
    print(smallestSubarraySumGreatherEqualK([2,1,5,1,3,2],6))
    print(smallestSubarraySumGreatherEqualK([2,3,4,1,5],2))
    print(smallestSubarraySumGreatherEqualK([2,1,5,2,3,2],7))


#  Find a subarray of length K with max sum 

def subarraySumK(nums: List[int], k: int) -> List[int]:
    windowStart = 0
    res = []
    sM = 0
    for windowEnd in range(len(nums)):
        if windowEnd-windowStart == k-1:
            s = sum(nums[windowStart:windowEnd+1])
            if s > sM:
                res = nums[windowStart:windowEnd+1]
                sM = s 
            windowStart +=1
    return res 

def runSubarraySumK():
    print(subarraySumK([2,1,5,1,3,2],3))
    print(subarraySumK([2,3,4,1,5],2))


# smallest subarray with a sum >=K

def smallestSubarrayLengthSumGreatherEqualK(nums: List[int], k: int) -> List[int]:
    windowStart = 0
    windowEnd = 0
    resLen = float("+inf")
    subarraySum = 0
    for windowEnd in range(len(nums)):
        subarraySum += nums[windowEnd]
        while subarraySum>=k:
            resLen = min(resLen, windowEnd-windowStart+1)
            subarraySum -= nums[windowStart]
            windowStart+=1
        else:
            windowEnd+=1

    return 0 if resLen == float("+inf") else resLen

def runsmallestSubarrayLengthSumGreatherEqualK():
    print(smallestSubarrayLengthSumGreatherEqualK([2,3,1,2,4,3],7))
    print(smallestSubarrayLengthSumGreatherEqualK([2,3,4,1,5],2))
    print(smallestSubarrayLengthSumGreatherEqualK([2,1,5,2,3,2],7))


if __name__ == "__main__":
    runsmallestSubarrayLengthSumGreatherEqualK()
