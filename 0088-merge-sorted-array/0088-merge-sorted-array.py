class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = m
        while j < (n+m):
            nums1[j]= nums2[i]
            i += 1
            j += 1
        nums1.sort()
        
        return nums1
        
            
            
            
                            

            
            
        
        
       
        
   