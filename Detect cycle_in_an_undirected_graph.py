from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		
		graph = defaultdict(list)
		indgree = [0]*V
		for i in range(V):
		    graph[i]=adj[i]
		    indgree[i] = len(adj[i])
		    
		q = deque()
		visited = set()
		for i in range(len(indgree)):
		    if indgree[i] == 1  or indgree[i] == 0:
		        q.append(i)
		        visited.add(i)
		
		while q:
		    ind = q.popleft()
		    
		    for node in graph[ind]:
		        indgree[node] -= 1
		        
		        if indgree[node] == :
		            if node not in visited:
		                visited.add(node)
		                q.append(node)
		                
	    for i in range(V):
	        if i not in visited:
	            return 1
	    return 0         
		                
		            
		        
		
		
		        
		        
		    
		
		


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
