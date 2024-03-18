class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt_sum = 0
        
        def post_order_traversal(node):
            nonlocal tilt_sum
            
            if not node:
                return 0
            
            left_sum = post_order_traversal(node.left)
            right_sum = post_order_traversal(node.right)
            
            tilt_sum += abs(left_sum - right_sum)
            
            return left_sum + right_sum + node.val
        
        post_order_traversal(root)
        
        return tilt_sum
