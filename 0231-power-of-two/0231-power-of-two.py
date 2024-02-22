class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is positive and not zero
        if n <= 0:
            return False

        # Check if n is equal to 1
        if n == 1:
            return True

        # Divide n by 2 until it becomes 1 or an odd number
        while n % 2 == 0:
            n = n // 2

        # Check if n is equal to 1
        if n == 1:
            return True
        else:
            return False
