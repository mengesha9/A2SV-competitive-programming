class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:


        memo = defaultdict(int)
        n = len(questions)

        def dp(ind):
            if ind >= n:
                return 0
                
            if ind not in memo:
                memo[ind] = max(questions[ind][0] + dp(ind + 1 + questions[ind][1] ) ,  dp(ind + 1) ) 

            return memo[ind]

       

        return dp(0)