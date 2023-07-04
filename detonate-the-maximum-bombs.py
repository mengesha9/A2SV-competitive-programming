class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i != j:
                    dis = (bombs[j][0] - bombs[i][0])**2 + (bombs[j][1] - bombs[i][1])**2
                    if dis <= (bombs[i][2] ** 2):
                        graph[i].append(j)
        
        def dfs(node, visit):
            visit.add(node)
            count = 1
            for neighbor in graph[node]:
                if neighbor not in visit:
                    count += dfs(neighbor, visit)
            return count
        
        ans = 0
        for i in range(n):
            visit = set()
            ans = max(ans, dfs(i, visit))
        
        return ans