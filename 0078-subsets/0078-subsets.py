class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def sub(index, arr):
            result.append(arr.copy())

            if len(nums) == index:
                return
            for i in range(index,len(nums)):
                arr.append(nums[i])
                sub(i + 1, arr)
                arr.pop()    

        sub(0,[])
        return result     
        