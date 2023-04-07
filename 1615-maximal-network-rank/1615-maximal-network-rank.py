class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        freq = defaultdict(set)
        for i in range(len(roads)):
            freq[roads[i][0]].add(roads[i][1])
            freq[roads[i][1]].add(roads[i][0])
        
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = len(freq[i]) + len(freq[j])
                if i in freq[j]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank
