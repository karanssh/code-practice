class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]  # Initialize stack with root node
    
    while stack:
        # Pop the top node from stack
        node = stack.pop()
        
        # Process current node
        result.append(node.val)
        
        # Push right child first (so left is processed first since it's a stack)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# Example usage:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(dfs_iterative(root))  # Output: [1, 2, 4, 5, 3]