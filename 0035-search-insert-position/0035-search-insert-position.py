class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers
        left = 0
        right = len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If the target is not found, return the index where it would be inserted
        return left
