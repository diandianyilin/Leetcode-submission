class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer to keep track of the current element
        current_ptr = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to the value to remove,
            # assign it to the current pointer position and move the pointer forward
            if nums[i] != val:
                nums[current_ptr] = nums[i]
                current_ptr += 1

        # Return the number of elements that are not equal to the value
        return current_ptr
      