class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(hour):
            count = 0
            for i in range(len(piles)):
                if(piles[i] <= hour):
                    count+=1
                else:
                    count += math.ceil(piles[i]/hour)        
            return count            
            
            

        low,high, best = 1, max(piles), 1
        while(low<=high):
            mid = low + (high-low)//2
            if(helper(mid) > h):
                low= mid +1
            else:
                high = mid -1
                best = mid
        return best






    

