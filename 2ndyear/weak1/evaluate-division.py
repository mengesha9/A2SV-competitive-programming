class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((values[i],equations[i][1]))
            graph[equations[i][1]].append((1/values[i],equations[i][0]))

           

        def bfs(node,ref):

            q = deque()
            q.append((1,node))
            visit = set()
            visit.add(node)

            while q:
                dis , k = q.popleft()
                if k == ref:
                    return dis
                print("hello")
                for d,n in  graph[k]:
                    if n not in visit:
                        visit.add(n)
                        
                        q.append((dis*d,n))
                        
 
            return - 1

        ans = []
        for u,v in queries:
        
            if u not in  graph or  v not in graph :
                ans.append(-1)
            
            else:
                ans.append(bfs(u,v))

        return ans         





        