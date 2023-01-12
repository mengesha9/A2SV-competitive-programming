class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
       
        left=0
        right=len(nums)-1
        newarr=[] 
        while left<=right:
            if left==right:
                newarr.append(nums[left])
                break
            else:      
                newarr.append(nums[right])
                newarr.append(nums[left])
                left+=1
                right-=1
        return newarr            
                
