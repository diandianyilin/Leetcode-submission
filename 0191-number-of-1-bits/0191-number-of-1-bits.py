class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            # Increment count if the least significant bit is 1
            count += n & 1
            # Shift n to the right by 1 bit
            n >>= 1

        return count
