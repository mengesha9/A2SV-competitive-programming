class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        arr=[]
        for i in range(len(operations)):
            if operations[i]=='C':
                arr.pop()
            elif operations[i]=="D":
                y=arr.pop()
                x=y*2
                arr.append(y)
                arr.append(x)
            elif  operations[i]=="+":
                y=arr.pop()
                x=arr.pop()
                arr.append(x)
                arr.append(y)
                arr.append(x+y)
            else:
                arr.append(int(operations[i]))
        count=0       
        for i in range(len(arr)):
            count+=arr[i]
        return count    
            
                
                
        
        
        
        
        
        
        
        
        
        