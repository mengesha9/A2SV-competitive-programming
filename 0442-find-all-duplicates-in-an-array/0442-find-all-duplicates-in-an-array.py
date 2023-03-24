class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        arr = []
        i = 0
        freq = defaultdict(int)
        while i < len(nums):
            
            if nums[i] != i+1:
                postion = nums[i] - 1
                if nums[postion] ==nums[i]:
                    if nums[i] not in freq:
                        arr.append(nums[i])
                        freq[nums[i]] += 1
                    
                    i += 1
                else:
                    nums[postion], nums[i]= nums[i], nums[postion] 
            else:
                i += 1        

        print(nums)        
        return arr           





