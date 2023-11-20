class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = defaultdict(int)
        for i,v in enumerate(nums):
            if target - v in freq:
                return [freq[target-v], i]
            freq[v] = i

        

            



                  

                



        
     
       
        
        
    
       
                
                        
        