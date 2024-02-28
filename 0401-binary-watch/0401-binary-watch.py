class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(num):
            return bin(num).count('1')
        
        result = []
        
        for hour in range(12):
            for minute in range(60):
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    result.append(f"{hour}:{minute:02}")
        
        return result