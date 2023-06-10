class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-1*x  for x in stones]
        heapq.heapify(heap)
        print(heap)

        while heap:
            val1 = -heapq.heappop(heap)
            if not heap:
                return val1
            val2 = -heapq.heappop(heap)
            if val1>val2:
                heapq.heappush(heap,val2-val1)

        if len(heap)>0:
            return heap[0]
        return 0