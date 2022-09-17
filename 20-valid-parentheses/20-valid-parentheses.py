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
    # def isValid(self, s):
    #     stack=[]
    #     for i in range(len(s)):
    #         if s[i]=='(' or s[i]=='[' or s[i]=='{' :
    #             stack.append(s[i])
    #         elif stack :
    #             if stack[-1]==']' or stack[-1]==')' or stack[-1]=='}':
    #                 stack.pop()
    #             return stack
    #         else:
    #             return False
    #     return stack==[]

    # def isValid(self,s):
    #     stack=[]
    #     hash_close={')':'(','}':'{',']':'['}
    #     for p in s:
    #         if p in hash_close.values():
    #             stack.append(p)
    #         elif stack and hash_close[p]==stack[-1]:
    #             stack.pop()               
    #         else:
    #             return False
    #     return stack==[]

            
            

                
                
                
        
        