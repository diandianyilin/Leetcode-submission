class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def in_order_traverse(node):
            nonlocal min_diff, prev_val
            
            if not node:
                return
            
            in_order_traverse(node.left)
            
            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)
                
            prev_val = node.val
            
            in_order_traverse(node.right)
        
        min_diff = float('inf')
        prev_val = None
        
        in_order_traverse(root)
        
        return min_diff
