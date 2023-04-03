class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        count = 0
        dic = defaultdict(int)
        while j < len(nums):
            if nums[j] not in dic :
                dic[nums[j]] += 1
                nums[i] ,nums[j] = nums[j],nums[i]
                i += 1
              
            
            else: 
                nums[j] = 0
                count += 1
        
            j += 1 

        return len(nums)-count          


        