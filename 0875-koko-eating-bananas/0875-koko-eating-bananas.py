class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def helper(mid):
            hour=0
            for pile in piles:
                if pile <=mid:
                    hour+=1
                else:
                    hour+=(math.ceil(pile/mid))
            return hour        

        j=max(piles)
        i=1
        best = -1
        while i<=j:
            mid=i+(j-i)//2
            if helper(mid)>h:
                i=mid+1
            elif helper(mid)<=h:
                best = mid
                j=mid-1
        return best        







    

