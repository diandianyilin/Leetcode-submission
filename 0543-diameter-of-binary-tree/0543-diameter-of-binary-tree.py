class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def maxDepth(node):
            if not node:
                return 0
            
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            
            self.diameter = max(self.diameter, left + right)
            
            return max(left, right) + 1
        
        maxDepth(root)
        
        return self.diameter
