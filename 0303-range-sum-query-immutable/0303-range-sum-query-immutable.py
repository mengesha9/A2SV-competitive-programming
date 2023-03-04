class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.presum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.presum[i+1]=nums[i]+self.presum[i]
          
    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)