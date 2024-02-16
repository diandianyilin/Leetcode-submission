class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate the height of a binary tree
        def height(node):
            # Base case: if the node is None, the height is 0
            if node is None:
                return 0

            # Recursive case: return the maximum height of the left and right subtrees, plus 1 for the current node
            return max(height(node.left), height(node.right)) + 1

        # Base case: if the root is None, the tree is height-balanced
        if root is None:
            return True

        # Check if the heights of the left and right subtrees differ by at most 1,
        # and both the left and right subtrees are height-balanced
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
     