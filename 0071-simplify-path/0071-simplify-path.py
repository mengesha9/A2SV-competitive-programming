class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        
        path=path.split("/")
        print(path)
        
        stack=[]
        for i in range(len(path)):
            if path[i]=='.' or path[i]=='':
                continue
            elif path[i]=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(path[i])
        if len(stack)==0:
            return '/'
        return  '/'+'/'.join(stack)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         path=path.split("/")
#         path=[a for a in path if a!=""]
#         arr=[]
#         v=''
#         for i in range(len(path)):
            
#             if arr and path[i]=='/' and arr[-1]==path[i]:
#                 arr.pop()
#                 arr.append(path[i])
#             if path[i]=='..' or path[i]=='.':
#                 continue
#             else:
#                 arr.append(path[i])
#         if len(arr) >0 and arr[-1] =='/' :
#             arr.pop()
                
#         for i in range(len(arr)) :
#             v+=arr[i]
#         return v    
            
                
                
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         p=path.split("/")
#         p=[a for a in p if a!=""]
#         stack=[]
#         for c in p:
#             if c =='.':
#                 continue
#             elif c=='..':
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(c)
#         return '/'+'/'.join(stack)        
                
        
        