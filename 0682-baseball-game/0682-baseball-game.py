class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        arr=[]
        for i in range(len(operations)):
            if operations[i]=='C':
                arr.pop()
            elif operations[i]=="D":
                arr.append(2*arr[-1])
                # y=arr.pop()
                # x=y*2
                # arr.append(y)
                # arr.append(x)
            elif  operations[i]=="+":
                
                arr.append(arr[-1]+arr[-2])
                
                # y=arr.pop()
                # x=arr.pop()
                # arr.append(x)
                # arr.append(y)
                # arr.append(x+y)
            else:
                arr.append(int(operations[i]))
        return sum(arr) 
            
                
                
        
        
        
        
        
        
        
        
        
        