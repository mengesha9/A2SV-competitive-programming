class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]])-> List[bool]:

        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)

        def findPre(a):
            arr = [False]*numCourses
            q = deque()
            q.append(a)
            visited = set()
            visited.add(a)
            while q:
                node = q.popleft()
                arr[node] = True
    
                for p in graph[node]:
                    if p not in visited:
                        visited.add(p)
                        q.append(p)

            return arr             

        ans = []
        for i in range(numCourses):
            ans.append(findPre(i))

        print(ans)    

        result = []
        for u, v in queries:
            
            result.append(ans[u][v])


        return result