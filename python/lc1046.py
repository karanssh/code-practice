import heapq
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    h = [] 
    for n in stones:
        heapq.heappush(h, -n)
    print(stones)
    while len(h) > 1:
        x = heapq.heappop(h)
        y = heapq.heappop(h)
        if x != y:
            heapq.heappush(h, abs(x - y))
    print(h)
    return h[0] if h else 0


print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([3,2,1,5,6,4]))
