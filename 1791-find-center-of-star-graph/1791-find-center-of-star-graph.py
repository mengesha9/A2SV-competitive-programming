class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        freq = defaultdict(int)
        for i in range(len(edges)):
            freq[edges[i][0]]  += 1
            freq[edges[i][1]]  += 1


        for k,v in freq.items():
            if v == len(edges):
                return k
                
