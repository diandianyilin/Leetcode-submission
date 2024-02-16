class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the array is empty, return None
        if not nums:
            return None

        # Find the middle element of the array
        mid = len(nums) // 2

        # Create a new node with the middle element as the value
        root = TreeNode(nums[mid])

        # Recursively construct the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        # Return the root node
        return root
