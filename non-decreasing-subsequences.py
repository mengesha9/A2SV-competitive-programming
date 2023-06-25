class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        result = []
        n = len(nums) 
        def back(ind,arr):
            if ind <= len(nums) and len(arr)>=2:
                if arr not in result:
                    result.append(arr.copy())
                if ind == len(nums):
                    return 

            for i in range(ind,n):
                if not arr:
                    arr.append(nums[i])
                    back(i+1,arr)
                    arr.pop()

                elif arr and nums[i]>=  arr[-1]:
                    arr.append(nums[i])
                    back(i+1,arr)
                    arr.pop()
                else:
                    back(i+1,arr)

        back(0,[])

        return result