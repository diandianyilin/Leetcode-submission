class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the last index of each number
        num_index = {}

        # Iterate through the array
        for i in range(len(nums)):
            # Check if the number already exists in the dictionary
            if nums[i] in num_index:
                # Check if the difference between the current index and the last index of the number is less than or equal to k
                if i - num_index[nums[i]] <= k:
                    return True
            # Update the last index of the number in the dictionary
            num_index[nums[i]] = i

        # No duplicates found within the given constraints
        return False
