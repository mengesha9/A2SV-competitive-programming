class Solution:
    def mySqrt(self, x: int) -> int:  
        i=0
        j=x
        if x==0 or x==1:
            return x
        ans=-1
        while i<=j:
            mid=i+(j-i)//2
            if mid*mid>x:
                j=mid-1
            else:
                ans=mid
                i=mid+1
        return ans        

  


