class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        
        for c in nums:
            if c == 0: red += 1
            if c == 1: white += 1
            if c == 2: blue += 1
        
        i = 0
        
        while red:
            nums[i] = 0
            red -= 1
            i += 1
        
        while white:
            nums[i] = 1
            white -= 1
            i += 1
        
        while blue:
            nums[i] = 2
            blue -= 1
            i += 1
        