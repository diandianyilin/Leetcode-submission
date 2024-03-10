class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        result = ""
        is_negative = num < 0
        num = abs(num)
        
        while num > 0:
            num, remainder = divmod(num, 7)
            result = str(remainder) + result
        
        if is_negative:
            result = "-" + result
        
        return result
