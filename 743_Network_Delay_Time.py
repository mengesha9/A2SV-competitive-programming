class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
            

        # distance = {node : float("inf") for node , v in graph.items()}
        t = 0

        min_heap = [(0,k)]
        visited = set()
        while min_heap:
            delay, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            t =max(t,delay)
            for neighbor , time in graph[node]:
                if neighbor not in visited:

                    heapq.heappush(min_heap,(time + delay,neighbor))

        return t if len(visited)==n else -1








        
