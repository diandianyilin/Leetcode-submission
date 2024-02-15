class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False

            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)

            return left and right

        return isSame(p, q)
 