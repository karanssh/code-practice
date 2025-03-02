import heapq
from typing import List 

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(n) for n in nums]
        h = []
        for n in nums:
            if len(h) == k:
                heapq.heappushpop(h, n)
            else:
                heapq.heappush(h, n)
        return str(heapq.heappop(h))
    
if __name__ == "__main__":
    ob = Solution()
    
    print(ob.kthLargestNumber(["1","2","3","4"],2))