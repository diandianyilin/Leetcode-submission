class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preorder(root, result)
        return result

    def preorder(self, node: TreeNode, result: List[int]) -> None:
        if node is None:
            return

        # Visit the current node
        result.append(node.val)

        # Traverse the left subtree
        self.preorder(node.left, result)

        # Traverse the right subtree
        self.preorder(node.right, result)
