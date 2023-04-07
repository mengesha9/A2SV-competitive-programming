class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        freq = [0]*n
        for i in range(len(edges)):
            freq[edges[i][1]] += 1
        ans = []
        for i in range(len(freq)):
            if freq[i] == 0:
                ans .append(i)
        return ans        




        