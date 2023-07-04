class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxor = 0
        for n in nums:
            maxor |= n

        length = len(nums)
        self.res = 0
        def back(ind, curr):
            if curr == maxor:
                self.res += 1
                if ind >= length:
                    return 
            tmp = curr
            for i in range(ind,length):
                curr |=  nums[i]
                back(i+1, curr)
                curr = tmp 

        back(0,0) 
        return self.res