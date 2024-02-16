class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the minimum depth is 0
        if root is None:
            return 0

        # Case 1: if the root has no left child, find the minimum depth of the right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1

        # Case 2: if the root has no right child, find the minimum depth of the left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1

        # Recursive case: find the minimum depth of the left and right subtrees
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # Return the minimum depth of the tree
        return min(left_depth, right_depth) + 1
