class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the carry and result variables
        carry = 0
        result = []

        # Iterate through the binary strings from right to left
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            # Get the current digits of a and b
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum of the current digits and the carry
            current_sum = digit_a + digit_b + carry

            # Determine the current digit of the result and the carry for the next iteration
            result.append(str(current_sum % 2))
            carry = current_sum // 2

            # Move to the next digits of a and b
            i -= 1
            j -= 1

        # If there is a remaining carry, add it to the result
        if carry:
            result.append(str(carry))

        # Reverse the result and return it as a binary string
        return ''.join(result[::-1])
      