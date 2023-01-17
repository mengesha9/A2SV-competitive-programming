class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        arr=[]
        x=[]
        for i in range(len(nums)):
            if nums[i] not in x:
                arr.append([nums.count(nums[i]),nums[i]])
                x.append(nums[i])
        arr.sort()
        res=[]
        i=len(arr)-1
        while k>0:
            
            res.append(arr[i][-1])
            i-=1
            k-=1
        return res
       
