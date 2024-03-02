class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        
        for i in range(max(len(num1), len(num2))):
            digit1 = num1[len(num1)-i-1] if i < len(num1) else 0
            digit2 = num2[len(num2)-i-1] if i < len(num2) else 0
            sum_digit = int(digit1) + int(digit2) + carry
            carry = sum_digit // 10
            result = str(sum_digit % 10) + result
        
        if carry > 0:
            result = str(carry) + result
        
        return result
