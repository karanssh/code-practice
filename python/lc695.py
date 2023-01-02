from typing import List 

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    visited = set() 
    maxArea = 0
    curArea = 0

    directions = [[0,1], [0,-1],[1,0], [-1,0]]
    
    def dfs(r, c):
        nonlocal curArea
        if r<0 or r ==R or c<0 or c==C or grid[r][c]==0 or (r,c) in visited:
            return
        
        curArea +=1 
        grid[r][c] = -1
        visited.add((r,c)) 
        for direction in directions:
            newR = r + direction[0]
            newC = c + direction[1]
            dfs(newR, newC)
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                dfs(i, j)
                maxArea = max(maxArea, curArea)
                curArea = 0
    
    return maxArea 


print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
