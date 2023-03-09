class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        i,j=0,len(nums)-1
        mid=0
        if target not in nums:
            return [-1,-1] 
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]>target:
                j=mid-1
            elif nums[mid]<target:
                i=mid+1
            else:
                break 
        h=mid
        k=mid
        while h<len(nums)-1 and nums[h+1]==target:
            h+=1
        while k-1>=0 and nums[k-1]==target:
            k-=1
        return [k,h]    





      