class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = [0]*n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u]+=1
            indegree[v]+=1

        q = deque()

        for i in range(len(indegree)):
            if indegree[i]==1:
                q.append(i)
                
        
        while n>2:
            n -= len(q)
            length = len(q)
            
            for i in range(length):
                node = q.popleft()
                for v in graph[node]:
                    indegree[v] -= 1
                    indegree[node] -= 1
                    
                    if indegree[v] == 1:
                        q.append(v)

        return list(q)