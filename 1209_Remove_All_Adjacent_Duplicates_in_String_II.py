class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        i = 0
        while i < len(s):
            
            if stack and stack[-1][0] == k-1 and s[i] == stack[-1][1]:
                stack.append([0,s[i]])
                count = k         
                while  count > 0:
                    stack.pop()
                    count -= 1
            else:
                if stack and stack[-1][1] == s[i]:
                    stack.append([stack[-1][0]+1,s[i]])
                else:
                    stack.append([1,s[i]])
            i += 1 


        return   "".join(stack[i][1] for i in range(len(stack)))


            
        
