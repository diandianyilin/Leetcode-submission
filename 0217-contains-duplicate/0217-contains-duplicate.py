class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store unique values
        unique_nums = set()

        # Iterate through the array
        for num in nums:
            # If the current value is already in the set, return True
            if num in unique_nums:
                return True

            # Add the current value to the set
            unique_nums.add(num)

        # If no duplicate is found, return False
        return False
