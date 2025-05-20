# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        level = 0
        while q:
            curLevel = []
            for i in range(len(q)):
                cur = q.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            if level%2==0:
                res.append(curLevel)
            else:
                curLevel = curLevel[::-1]
                res.append(curLevel)
            level +=1
        return res