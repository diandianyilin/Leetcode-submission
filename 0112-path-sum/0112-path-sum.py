class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the root is None, return False
        if root is None:
            return False

        # Base case: if the root is a leaf node and its value equals the targetSum, return True
        if root.left is None and root.right is None and root.val == targetSum:
            return True

        # Recursive case: check if there is a root-to-leaf path with the targetSum in the left or right subtree
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
