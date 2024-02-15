# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node is None:
                return []

            left = inorder(node.left)
            left.append(node.val)
            right = inorder(node.right)

            return left + right

        return inorder(root)
