class Solution:
    def isValid(self,s):
        stack=[]
        hashMa_close={'(':')','[':']','{':'}'}
        for bracket in s:
            if bracket in hashMa_close.keys():
                stack.append(bracket)
            elif stack==[] or bracket != hashMa_close[stack.pop()]:
                return False
        return stack == []  
                
                
                
        
        