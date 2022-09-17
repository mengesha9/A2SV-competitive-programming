class Solution:
    def isValid(self,s):
        stack = []
        close_parentheses = {')': '(', '}': '{', ']': '['}
        for p in s:
            if p in close_parentheses.values():
                stack.append(p)
            elif stack and close_parentheses[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == [] 

            
            

                
                
                
        
        