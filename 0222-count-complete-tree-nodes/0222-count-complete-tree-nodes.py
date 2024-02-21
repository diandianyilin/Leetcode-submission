# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, return 0
        if root is None:
            return 0

        # Calculate the height of the left and right subtrees
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        # If the height of the left subtree is equal to the height of the right subtree,
        # it means the left subtree is a complete binary tree.
        if left_height == right_height:
            # Count the number of nodes in the left subtree using the formula 2^left_height - 1
            # and recursively count the number of nodes in the right subtree
            return (1 << left_height) + self.countNodes(root.right)

        # If the height of the left subtree is greater than the height of the right subtree,
        # it means the right subtree is a complete binary tree.
        else:
            # Count the number of nodes in the right subtree using the formula 2^right_height - 1
            # and recursively count the number of nodes in the left subtree
            return (1 << right_height) + self.countNodes(root.left)

    def get_height(self, node: Optional[TreeNode]) -> int:
        # Helper function to calculate the height of a binary tree
        height = 0
        while node:
            height += 1
            node = node.left
        return height
