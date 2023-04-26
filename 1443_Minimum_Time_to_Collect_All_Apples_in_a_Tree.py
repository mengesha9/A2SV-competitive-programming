class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if len(edges)==0:
            return 0
        adjlist = defaultdict(list)

        for edge in edges:
            adjlist[edge[0]].append(edge[1])
            adjlist[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)    
            if not adjlist[node] and hasApple[node]:
                if hasApple[node]:
                    return 2
                else:
                    return 0
                    
            count = 0
            for k in adjlist[node]:
                count += dfs(k)

            if (node != 0 )and ( count > 0 or hasApple[node]):
                count += 2    
            return count 
            
        return dfs(0)
