class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        while q:
            val = q.popleft()
            order.append(val)
            for node in graph[val]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        if len(order)==numCourses:
            return True 
        return False