class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        
        ans = 0
        time=tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] < time:
                    ans += tickets[i]
                else:
                    ans += time
            else:
                if tickets[i] < time:
                    ans +=  tickets[i] 
                else:
                    ans += time - 1
                    
                
        return ans       
                
                    
                
        