class Solution:
    def mySqrt(self, x: int) -> int:
        # Check for base cases
        if x == 0 or x == 1:
            return x

        # Perform binary search to find the square root
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        # Return the floor of the square root
        return right
