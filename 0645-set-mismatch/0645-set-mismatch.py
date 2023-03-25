class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        arr = []
        i = 0
        while i<len(nums):
            if nums[i] != i+1:
                postion = nums[i]-1
                if nums[postion] == nums[i]:
                    i += 1
                else:
                    nums[postion],nums[i] = nums[i],nums[postion]
            else:
                i += 1


        for i in range(len(nums)):
            if nums[i] != i+1:
                arr.append(nums[i])
                arr.append(i+1)
                return arr 
                         

        