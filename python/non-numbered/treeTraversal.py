# Definition for a binary tree node.

from typing import List, Optional 
from collections import defaultdict
from collections import Counter



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        st = []
        res = []
        cur = root

        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                curNode = st.pop()
                res.append(curNode.val)
                cur = curNode.right
        
        return res
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        st = [root]
        res = []

        while st:
            curNode = st.pop()
            res.append(curNode.val)
            if curNode.right:
                st.append(curNode.right)
            if curNode.left:
                st.append(curNode.left)
        return res

    