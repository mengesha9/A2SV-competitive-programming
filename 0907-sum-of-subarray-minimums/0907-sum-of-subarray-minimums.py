class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:


        arr.append(0)
        stack=[]
        ans=0
        for i,val in enumerate(arr):
            left_bound = i
            while stack and arr[stack[-1][0]]>val:
                curr , left =stack.pop()
                left_bound = left
                subarray=(i-curr)*(curr-left + 1)
                ans += (arr[curr]*subarray)
            stack.append((i,left_bound))
      
        return ans  %  (10**9 + 7)  






