class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # Shift the result to the left by 1 bit
            result <<= 1
            # Get the least significant bit of n and add it to the result
            result |= n & 1
            # Shift n to the right by 1 bit
            n >>= 1

        return result
       