class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        count = 0
        for i in s:
            if i == ')':
                temp = 0
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                if temp == 0:
                    stack.append(1)
                else:
                    stack.append(2*temp)
            else:
                stack.append(i)        

        return sum(stack)        




        