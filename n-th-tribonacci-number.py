class Solution:
    def tribonacci(self, n: int) -> int:
        
        arr=[0]*38
        arr[0]=0
        arr[1]=1
        arr[2]=1
        
        for i in range(3,len(arr)) :
            arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
        print(arr)    
        return arr[n]  
        
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         a=0
#         b=1
#         c=1
        
#         for i in range(n):
#             a,b,c=b,c,a+b
#         return a    
        
        
        
#         if n==0:
#             return 0
#         if n==1 or n==2:
#             return 1
        
#         return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)