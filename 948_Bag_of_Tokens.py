class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        score=0
        i=0
        j=len(tokens)-1
        tokens.sort()
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                score+=1      
            elif score>=1 and power <tokens[i] and j-i>1: 
                    power+=tokens[j]
                    score-=1
                    j-=1 
                    i-=1
            i+=1            
        return score        
                
