class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        j=0
        i=0
        _sum=0
        leng=float("inf")
        while j<len(nums):
            _sum+=nums[j]
            while _sum>=target and i<len(nums):
                _sum-=nums[i]
                leng=min(leng,j-i+1)
                i+=1
            j+=1  
        return leng if leng != float("inf") else 0    
       


     




            


                




     
        
