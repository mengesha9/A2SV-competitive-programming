import heapq
from collections import defaultdict

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.counts = defaultdict(int)
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.counts[val] += 1
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, (val, self.counts[val]))
        else:
            if self.heap[0][0] < val or (self.heap[0][0] == val and self.heap[0][1] < self.counts[val]):
                _, count = heapq.heappushpop(self.heap, (val, self.counts[val]))
                self.counts[val] = count
        return self.heap[0][0]