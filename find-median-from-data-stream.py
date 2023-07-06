class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap,num)
        val = heapq.heappop(self.minheap)
        heapq.heappush(self.maxheap,-val)

        if len(self.maxheap)-len(self.minheap)>1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-val)




    def findMedian(self) -> float:
        median = -self.maxheap[0] 
        if len(self.maxheap) == len(self.minheap):
            median = (self.minheap[0]+median)/2
        
        return median   







        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()