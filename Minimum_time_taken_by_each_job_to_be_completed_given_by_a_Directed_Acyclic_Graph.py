from typing import List
from collections import defaultdict , deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        
        indgree = [0]*n
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            indgree[v-1] += 1
            
        q = deque()
      
        output = [float("inf")]*n
        
        for i in range(len(indgree)):
            if indgree[i] == 0:
                q.append((i+1,1))
                
                output[i] = min(output[i],1)
        
        while q:
            ind, time = q.popleft()
            
            for node in graph[ind]:
                indgree[node-1] -= 1
                if indgree[node-1] == 0:
                    output[node-1] = min(output[node-1],time+1)
                    q.append((node,time+1))
                    
        return output            
                    
                    
                
                
                
        

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends
