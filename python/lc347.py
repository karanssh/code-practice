from typing import List 
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    c = Counter(nums)
    return [x for x, y in c.most_common(k)]
 


print(
    topKFrequent([1,1,2,2,3,44,5,5,5,5,6], 2)
)
