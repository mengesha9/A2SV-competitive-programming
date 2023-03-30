class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        count = 0
        while y > 0 or x > 0:
            if (y % 2 == 0 and x %2 != 0) or (y % 2 != 0 and x % 2 == 0):
                count += 1
            
            x = x >> 1
            y = y >> 1 

        return count            



