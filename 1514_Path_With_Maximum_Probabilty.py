class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((succProb[i],edges[i][1]))
            graph[edges[i][1]].append((succProb[i],edges[i][0]))

        distance = [1 for i in range(n) ]

        q = deque()
        max_heap = [(-1,start_node)]
        visit = set()
        while max_heap:
            pro, node = heapq.heappop(max_heap)
            if node in visit:
                continue
            visit.add(node) 

            for sucpro, n in graph[node]:
                if distance[n-1] >  pro*sucpro:
                    distance[n-1] = pro*sucpro
                    heapq.heappush(max_heap,(distance[n-1],n))

        return -distance[end_node-1] if distance[end_node-1] != 1 else 0.00000









        



        
