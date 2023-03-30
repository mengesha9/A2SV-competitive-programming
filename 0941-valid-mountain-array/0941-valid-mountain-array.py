class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:


        if len(arr)<3:
            return False

        for i in range(1,len(arr)-1):
            if arr[i-1] <arr[i]>arr[i+1]:
                l=i-1
                r=i+1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                if r==len(arr)-1 and l==0:
                    return True

        return False