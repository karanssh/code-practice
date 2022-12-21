from typing import List 
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    goodOranges = 0
    q = deque()
    timeTaken = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                goodOranges +=1 
            if grid[i][j] == 2:
                q.append((i, j))
    
    directions = [[0,1], [1,0], [-1,0], [0,-1]]
    while q and goodOranges>0:

        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                newRow, newCol = r+dr , c+dc 
                if (
                    newRow>=0 and newRow <R and
                    newCol>=0 and newCol < C and 
                    grid[newRow][newCol] == 1
                ):
                    grid[newRow][newCol] = 2 
                    q.append((newRow, newCol))
                    goodOranges -=1 
        timeTaken +=1
    
    if goodOranges == 0:
        return timeTaken
    
    return -1
    
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

