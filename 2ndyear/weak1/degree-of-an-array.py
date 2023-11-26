class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n]  += 1

        freq = max(count.values())
        
        dic = defaultdict(int)
        i = 0
        mindis = len(nums)
        for j in range(len(nums)):
            dic[nums[j]] += 1
            while dic and max(dic.values()) >= freq:
                mindis = min(mindis,j-i+1)

                dic[nums[i]] -=1
                i += 1

            
          
        
        return mindis          
        


        