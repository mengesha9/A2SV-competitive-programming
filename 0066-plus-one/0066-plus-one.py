class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
#         x=''.join(map(str,digits))
#         # print(x)   
#         y=int(x)
#         y+=1
#         # print(y)
        
#         y=str(y)
        
#         # print(y)
#         arr=[]
#         for i in range(len(y)):
#             arr.append(y[i])
#         return arr    
        
        digits=digits[::-1] 
        one=1
        i=0
        while one:
            if i<len(digits):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    one=0
            else:
                digits.append(1)
                one=0
            i+=1    
        return   digits[::-1]       
        