class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        res=0
        i=0
        j=k
       
        total=sum(nums[i:k])
        res=total/k
        while j<len(nums):
            total+=(nums[j]-nums[i])
            res=max(res,total/k)
            i+=1
            j+=1
        return res    




