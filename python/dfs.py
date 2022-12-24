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


def dfs(root: TreeNode):
    res = []
    def helper(root):
        if root is None:
            return 
        
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    print(res)

def pathSumEqualsK(root: TreeNode, k : int):
    
    def helper(root, s):
        if root is None:
            return False 
        if root.left is None and root.right is None and s == k:
            return True
        
        s += root.val
        return helper(root.left, s) or helper(root.right, s)
        
    hasSum = helper(root, 0)
    print(hasSum)

pathSumEqualsK(randomTree(), 13)
