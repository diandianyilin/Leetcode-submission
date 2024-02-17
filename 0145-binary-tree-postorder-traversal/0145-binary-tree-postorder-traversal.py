class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, node: TreeNode, result: List[int]) -> None:
        if node is None:
            return

        # Traverse the left subtree
        self.postorder(node.left, result)

        # Traverse the right subtree
        self.postorder(node.right, result)

        # Visit the current node
        result.append(node.val)
