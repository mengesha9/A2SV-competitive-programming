class Solution:
    def isValid(self, s: str) -> bool:
        
        
        dic={')':'(','}':'{',']':'['}
        arr=[]
        for br in s:
            if arr and br in dic and arr[-1] == dic[br]:
                arr.pop()
            else:
                arr.append(br)
        
        return True  if not arr else False  
                
                
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
#         brak={']':'[',')':'(','}':
#              '{'}
#         stack=[]

#         for c in s:
#             if stack and c in brak and  stack[-1]==brak[c]:
#                 stack.pop()
#             else:
#                 stack.append(c)
#         return True if not stack else False       
            