class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR all the elements in the array
        result = 0
        for num in nums:
            result ^= num

        return result
