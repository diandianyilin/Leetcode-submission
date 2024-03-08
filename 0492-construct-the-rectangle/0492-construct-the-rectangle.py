class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        
        sqrt_area = int(math.sqrt(area))
        
        for i in range(sqrt_area, 0, -1):
            if area % i == 0:
                return [area // i, i]
     