class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        ordlist = []
        for i in range(len(s)):
            ordlist.append((ord(s[i])-ord("a")+1))
        
        total = 0
        mul = 1
        for i in range(k):
            total = total + (ordlist[i]  *mul )
            mul = mul *power

        mul = mul//power
        for j in range(len(s)-k+1):
            if total % modulo == hashValue:
                return s[j:j+k]
            if j < len(s)-k:
                total = (total - ordlist[j]) // power + ordlist[j+k] *mul  
            
                    



        
        
