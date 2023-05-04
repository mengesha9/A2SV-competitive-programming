class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        
        di= defaultdict(int)
        for word in words:
            di[word]+= 1

        arr=[]
         
        for key,v in di.items():
            heapq.heappush(arr,(-v,key))


        ans = []
        while k:
            freq, word = heapq.heappop(arr)
            ans.append(word)
            k-=1
                

        return ans