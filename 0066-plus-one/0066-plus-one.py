class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        x=''.join(map(str,digits))
        # print(x)   
        y=int(x)
        y+=1
        # print(y)
        
        y=str(y)
        
        # print(y)
        arr=[]
        for i in range(len(y)):
            arr.append(y[i])
        return arr    
        
        