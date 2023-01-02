from typing import List 
from collections import deque, defaultdict

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:

    preMap = {i: [] for i in range(numCourses)}

    # map each course to : prereq list
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visiting = set()

    def dfs(crs):
        if crs in visiting:
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True



# print(
# canFinish(2,[[1,0],[0,1]])
# )

print(
canFinish(20,[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])
)

