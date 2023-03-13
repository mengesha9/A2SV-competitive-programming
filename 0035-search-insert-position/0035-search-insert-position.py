class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        i=0
        j=len(nums)-1
        if nums[i]==target:
            return i
        elif nums[j]==target:
            return j

        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1 

        return ((i+j)//2 )+1  