class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        string=''
        
        for c in s:
            if c=='(':
                stack.append(string)
                string=''
            elif c==')':
                string=stack.pop()+string[::-1]
            else:
                string+=c
        return string       
                

            
    
                

        