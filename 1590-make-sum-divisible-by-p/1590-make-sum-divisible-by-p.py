class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total_sum = sum(nums)
        target_rem = total_sum % p
        if target_rem == 0:
            return 0  # No need to remove any subarray

        prefix_sum = 0
        min_len = float('inf')
        prefix_map = {0: -1}  # {prefix_sum mod p : index}

        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_mod = prefix_sum % p

            # Find the required mod to make the rest divisible by p
            required_mod = (prefix_mod - target_rem) % p

            if required_mod in prefix_map:
                min_len = min(min_len, i - prefix_map[required_mod])

            # Update the prefix sum in the map
            prefix_map[prefix_mod] = i

        return min_len if min_len != float('inf') and min_len < len(nums) else -1
