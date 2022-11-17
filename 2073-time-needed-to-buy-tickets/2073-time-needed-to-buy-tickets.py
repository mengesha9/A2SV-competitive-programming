class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        value=tickets[k]
        count=0
        while value:
            
            for i in range(len(tickets)):
                if tickets[k] >0 and  tickets[i]>0:
                    tickets[i]-=1
                    count+=1
            value-=1        
        return count          
        
        
        
        
        