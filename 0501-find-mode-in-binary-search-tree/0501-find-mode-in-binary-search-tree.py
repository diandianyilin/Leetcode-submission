class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        modes = []
        prev = None
        curr_count = 0
        max_count = 0

        def inorder_traversal(node):
            nonlocal prev, curr_count, max_count, modes

            if not node:
                return

            inorder_traversal(node.left)

            if prev is None or prev != node.val:
                curr_count = 1
            else:
                curr_count += 1

            if curr_count > max_count:
                max_count = curr_count
                modes = [node.val]
            elif curr_count == max_count:
                modes.append(node.val)

            prev = node.val

            inorder_traversal(node.right)

        inorder_traversal(root)

        return modes
