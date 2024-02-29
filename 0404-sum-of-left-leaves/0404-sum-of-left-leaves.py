# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        
        if root is None:
            return 0
        
        total = 0
        
        if isLeaf(root.left):
            total += root.left.val
        
        total += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        return total
