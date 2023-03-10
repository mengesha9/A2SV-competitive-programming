class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.nums = nums
        self.res = []
        self.helper(0, [], len(self.nums))
        return self.res

    def helper(self, i, arr, n):

        if i>= n:
            self.res.append(arr.copy())
            return 
        arr.append(self.nums[i])
        self.helper(i+1, arr , n)
        
        arr.pop()
        
        self.helper(i+1, arr, n)


