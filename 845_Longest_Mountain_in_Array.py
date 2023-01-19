class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        if len(arr)<3:
            return 0
        length=0
        i=1
        while i<len(arr)-1:
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                l=i
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                    print(arr[l])
                r=i 
                while r+1<len(arr) and arr[r]>arr[r+1]:
                    r+=1
                    print(arr[r])
                length=max(length,r-l+1)   
                
            i+=1  
        return length            
