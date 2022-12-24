from typing import List 
def maxArea(height: List[int]) -> int:
    l , r = 0, len(height)-1
    res = 0 
    while l<r:
        w = r = l 
        h = min(height[l], height[r])
        area = h*w 
        res = max(res, area)
        if height[l]< height[r]:
            l +=1 
        elif height[l]>height[r]: r -=1
        else:
            l+=1 
            r -=1
    return res 
