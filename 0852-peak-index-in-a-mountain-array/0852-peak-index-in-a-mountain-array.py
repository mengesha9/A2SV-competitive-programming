class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        if len(arr)<3:
            return -1
        
        
        i , j  = 0, len(arr)-1
        while i<=j:
            mid = i + (j-i) // 2
            if arr [mid-1] < arr[mid] > arr[mid+1]:
               return mid
            elif arr[mid] < arr[mid+1]:
                i = mid + 1
            elif arr[mid-1] >  arr[mid]:
                j = mid - 1


                
                
        