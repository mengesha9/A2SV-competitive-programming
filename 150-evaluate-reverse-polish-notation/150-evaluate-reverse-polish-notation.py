class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+','-','/','*'}
        stack=[]
        
        for c in tokens:
            if c in operators:
                first_num=stack.pop()
                second_num=stack.pop()
                if c =='+':
                    stack.append(first_num+second_num)
                elif c=='/':
                    stack.append(int(second_num/first_num))
                elif c=='*':
                    stack.append(first_num*second_num)
                else:
                    stack.append(second_num-first_num)
            else:
                stack.append(int(c))
        return stack[-1]