class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                left=i-1
                break
        if left==-1:
            nums.sort() 
        right=len(nums)-1
        while right>=0 and nums[left]>=nums[right] :
            right-=1
        nums[right],nums[left]=nums[left],nums[right] 
        nums[left+1:]=sorted(nums[left+1:])

