class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Check if the array is empty
        if not nums:
            return 0

        # Initialize a pointer to keep track of the current unique element
        unique_ptr = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous unique element,
            # update the unique pointer and assign the current element to the unique pointer position
            if nums[i] != nums[unique_ptr]:
                unique_ptr += 1
                nums[unique_ptr] = nums[i]

        # Return the number of unique elements (unique pointer + 1)
        return unique_ptr + 1
