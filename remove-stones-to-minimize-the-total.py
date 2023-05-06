class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:


        heap = []
        for i in piles:
            heap.append(-i)
        heapq.heapify(heap)    
        while k>0:
            ind = heapq.heappop(heap)
            ind  =math.ceil(( -1*ind) /2)
            heapq.heappush(heap,-ind)
            k -= 1
        return   -sum(heap)