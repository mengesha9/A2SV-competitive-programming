class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        l=0
        r=len(y)-1
        output=False
        while l<=r:
            if y[l]!=y[r]:
                output= False
                break
            else:
                output=True
            l+=1
            r-=1
            
        return output