import heapq
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    h = [] 
    for n in nums:
        if len(h) == k:
            heapq.heappushpop(h, n)
        else:
            heapq.heappush(h, n)
    print(h)
    return heapq.heappop(h)

print(findKthLargest([9, 15, 20], 2))
print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 5))