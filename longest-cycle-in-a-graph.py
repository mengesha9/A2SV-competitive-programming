class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        graph = defaultdict(list)
        indegree = [0] * len(edges)
        outdegree = [0] * len(edges)

        for i in range(len(edges)):
            graph[i].append(edges[i])
            indegree[i] += 1
            outdegree[edges[i]] += 1

        arr = []
        for i in range(len(edges)):
            if indegree[i] > 0 and outdegree[i] > 0:
                arr.append(i)

        if len(arr) < 2:
            return -1
        
        visited = set()
        def dfs(k,dis, dic, cycle,cur):
            
            if k in cur:
                cycle[0] = max(cycle[0], dis-dic[k])
                return
            
            if k in visited:
                return 
            dic[k]=dis
            cur.add(k)
            visited.add(k)
            
            for v in graph[k]:
                if indegree[v] > 0 and outdegree[v] > 0:
                    dfs(v,dis+1,dic, cycle,cur)     

        cycle = [-1]
        for i in arr:
            if i not in visited:
                dfs(i, 0,defaultdict(), cycle,set())
                    

        return cycle[0]