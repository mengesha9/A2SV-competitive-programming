class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(heap)<k:
                    heapq.heappush(heap,-matrix[i][j])
                else:
                    if heap[0]<-matrix[i][j]:
                        heapq.heappop(heap)
                        heapq.heappush(heap,-matrix[i][j]) 

        return -heapq.heappop(heap)