class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ind = defaultdict(list)
        indegree = [0]*n
        anc = defaultdict(set)
        for u,v in edges:
            ind[u].append(v)
    
            indegree[v] += 1

        q = deque()    
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)


        while q:
             node = q.popleft()
             for val in ind[node]:
                indegree[val]-=1
                anc[val].add(node)
                for m in anc[node]:
                   anc[val].add(m)
                if indegree[val]==0:
                    q.append(val)

        answer = []
        for i in range(len(indegree)):
            if i not in anc:
                answer.append([])
            else:    
                tmp = list(anc[i])
                tmp.sort()
                answer.append(tmp)

        return answer