class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def helper(capa):
            count=0
            res=1
            for w in weights:
                count+=w
                if count>capa:
                    count = w
                    res+=1
            return res        

        i=max(weights)
        j=sum(weights)
        best=0
        while i<=j:
            capa=i+(j-i)//2
            if helper(capa)<=days:
                j=capa-1
                best=capa
            else:
                i=capa+1
        return best        

