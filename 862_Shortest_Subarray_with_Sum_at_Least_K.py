class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum=[0]*(len(nums)+1 )
        for i in range(len(nums)):
            
                presum[i+1]=nums[i]+presum[i]
              
        arr=[]
        res = float(inf)
        for i in range(len(presum)):
            
            while(arr and arr[-1][1] >=presum[i]):
                arr.pop()
            
            while arr and presum[i] - arr[0][1] >= k:
                res = min(i-arr[0][0], res)
                arr.pop(0)
                
            arr.append([i,presum[i]])
          
        return res if res!= float(inf) else -1  
