from typing import List 
from collections import deque 

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val 
        self.left, self.right = None, None
# right side view of a binary tree

def randomTree() ->TreeNode:
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.left.left.left = TreeNode(32)
    return root  


def bfs(root: TreeNode):
    res = []
    q = deque()
    q.append(root)

    while q:
        levelSize = len(q)
        resItem = []
        for _ in range(levelSize):
            curNode = q.popleft()
            resItem.append(curNode.val)
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)

        res.append(resItem)
    
    print(res)
    return res 

def rightSideView(root: TreeNode):
    res = []
    q = deque()
    q.append(root)

    while q:
        levelSize = len(q)
        resItem = []
        for _ in range(levelSize):
            curNode = q.popleft()
            resItem.append(curNode.val)
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)

        res.append(resItem[-1])
    
    print(res)
    return res 

rightSideView(randomTree())