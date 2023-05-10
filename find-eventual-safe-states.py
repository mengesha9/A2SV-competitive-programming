class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        adjlist = defaultdict(list)
        outdegree = [0]*len(graph)

        for i,v in enumerate(graph):
            for m in v:
                adjlist[i].append(m)
                adjlist[m].append(i)
                outdegree[i] += 1

        q = deque()        
        for i in range(len(graph)):
            if outdegree[i]==0:
                q.append(i)

        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for val in adjlist[node]:
                outdegree[val]-=1
                if outdegree[val]==0:
                    q.append(val)

        order.sort()

        return order