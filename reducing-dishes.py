class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxsat = -float("inf")

        for i in range(len(satisfaction)):
            total = 0
            for j in range(i, len(satisfaction)):
                total += (j-i+1)*satisfaction[j]
            maxsat = max(total,maxsat)
        

        return maxsat  if maxsat > 0 else 0