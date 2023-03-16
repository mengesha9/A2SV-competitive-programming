class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       
        result = []
        def comb(index,k,arr):
            
            if k == 0:
                result.append(arr.copy())
                return
            if index == n+1:
                return   
            for i in range(index,n+1):
                arr.append(i) 
                comb(i +1, k-1,arr)  
                arr.pop()

        comb(1,k,[]) 

        return result     



