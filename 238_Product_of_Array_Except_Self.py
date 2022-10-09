class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        i=1
        j=len(nums)-2
        pri_sum=[1]*len(nums)
        suf_sum=[1]*len(nums)
        while i<len(nums) and j>=0:
            pri_sum[i]=pri_sum[i-1]*nums[i-1]
            suf_sum[j]=suf_sum[j+1]*nums[j+1]
            i+=1
            j-=1
        output=[0]*len(nums)   
        for i in range(len(nums)):
            output[i]=pri_sum[i]*suf_sum[i]
        return output     
