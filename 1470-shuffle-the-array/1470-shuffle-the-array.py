class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr=[]
        for i in range(0,n):
           
            arr.append(nums[i])
            arr.append(nums[n])
            n+=1
        for i in range(len(nums)):
            nums[i]=arr[i]
            
        return nums   
        
        
       
            
        
        