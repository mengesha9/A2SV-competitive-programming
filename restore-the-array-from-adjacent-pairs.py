class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in adjacentPairs:
            indegree[u] += 1
            indegree[v] += 1
            graph[u].append(v)
            graph[v].append(u)
        q = deque()

        for k,v in indegree.items():
            if v == 1:
                q.append(k)
                break
        
        answer = []
        visit = set()
        while q:

            node = q.popleft()
            if node not in visit:
                visit.add(node)
                answer.append(node) 

            for p in graph[node]:
                if indegree[p] > 1:
                    indegree[p] -= 1
                if indegree[p] == 1:
                    indegree[p] -= 1
                    q.append(p)

        return answer