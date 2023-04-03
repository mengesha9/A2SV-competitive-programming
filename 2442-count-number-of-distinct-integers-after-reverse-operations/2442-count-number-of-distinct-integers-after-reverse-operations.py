class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        dist = set()
        for i in range(len(nums)):
            
            temp = self.reverse(nums[i])    
            dist.add(nums[i])
            dist.add(temp)
        return len(dist)        

    def reverse(self,number):
        reverse_number = 0

        while number > 0:
            remainder = number % 10
            reverse_number = (reverse_number * 10) + remainder
            number = number // 10
        return reverse_number     

