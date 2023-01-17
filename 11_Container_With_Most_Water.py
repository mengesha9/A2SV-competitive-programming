class Solution:
    def maxArea(self, height: List[int]) -> int:



        i=0
        j=len(height)-1
        maxarea=0
        while i<j:

            if height[j]>height[i]:
                maxarea=max(maxarea,height[i]*(j-i))
                i+=1
            else:
                maxarea=max(maxarea,height[j]*(j-i)) 
                j-=1
        return maxarea 
