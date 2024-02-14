class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the rightmost digit
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, increment it by one and return the digits
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            else:
                digits[i] = 0

        # If all digits are 9, add a new leading 1 to the digits
        digits.insert(0, 1)

        return digits
