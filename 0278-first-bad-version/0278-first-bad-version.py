# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        i=1
        j=n
        ans=float('inf')
        while i<=j:
            mid=i+(j-i)//2
            if isBadVersion(mid):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans 










    


        