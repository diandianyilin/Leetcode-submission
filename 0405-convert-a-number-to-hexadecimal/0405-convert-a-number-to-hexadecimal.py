class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        if num < 0:
            num += 2**32  # Convert negative number to its 32-bit two's complement equivalent
        
        while num > 0:
            digit = num % 16
            result = hex_chars[digit] + result
            num //= 16
        
        return result
