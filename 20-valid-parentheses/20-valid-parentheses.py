class Solution:
    def isValid(self, s: str) -> bool:
         
        brak={']':'[',')':'(','}':
             '{'}
        stack=[]

        for c in s:
            if stack and c in brak and  stack[-1]==brak[c]:
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False   
                
                
                
        
        
