class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n <=1:
            return 0
        self.ans = -1
        def rec(l,r):
            if l == r:
                return 
            mid = (l+r)//2

            if  mid == 0 and nums[mid] > nums[mid+1]:
                self.ans = mid
                return
            if  mid == n-1 and  nums[mid] > nums[mid-1]:
                self.ans = mid 
                return
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                self.ans = mid
                return   
            rec(l,mid)
            rec(mid+1,r)

        rec(0,n)

        return self.ans

                   

        