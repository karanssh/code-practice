import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            heapq.heappush(nums, heapq.heappop(nums)+1)
            k-=1
        
        res = 1
        for n in nums:
            res = (res * n) % (10**9+7)

        return res
        