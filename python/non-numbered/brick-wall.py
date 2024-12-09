from typing import List

def leastBricks(wall: List[List[int]]) -> int:
        c = {0:0}
        for r in wall:
            tot = 0 
            for b in r[:-1]:
                tot += b 
                c[tot] = 1 + c.get(tot, 0)
        print(c)
        

        m = max(c.values())
        return len(wall) - m

print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))