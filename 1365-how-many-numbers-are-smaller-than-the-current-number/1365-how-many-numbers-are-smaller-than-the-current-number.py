class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i!=j and nums[i] > nums[j] :
                        count +=1               
            arr.append(count)
        return arr   



# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
#         ar = [0 for i in range(max(nums) + 1)]
#         ar2 = nums[::]
#         nums.sort()
        
#         for i in range(len(nums)):
#             if i == 0:
#                 continue
            
#             if nums[i] > nums[i-1]:
#                 ar[nums[i]] = i
            
#             elif nums[i] == nums[i-1]:
#                 ar[nums[i]] = ar[nums[i-1]]
        
#         res = [0 for i in range(len(nums))]
        
#         for i in range(len(nums)):
#             res[i] = ar[ar2[i]]
        
#         return res