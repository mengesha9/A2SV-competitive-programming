class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)
        for u,v,d in roads:
            graph[u].append([v,d])
            graph[v].append([u,d])

        visit = set()
        def dfs(node):
            visit.add(node)
            dis = float("inf")
            for k,di in graph[node]:
                if k  not  in visit:
                    visit.add(k)
                    dis = min( dis,dfs(k))
                else:

                   dis = min(dis,di)
            return dis 

        return dfs(1)