class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        n = len(values)

        value = {}
        for i in range(len(values)):
            if i < n-1:
                value[i] = values[i+1:]

        dpvalue = defaultdict(int)
        def dp(ind):
            if ind == n - 2:
                 return  values[ind] + values[ind+1] + ind -( ind + 1) 

            if ind not in dpvalue:
                count = float("-Inf")

                for i in range(ind+1,n):
                    tmp = values[ind] + values[i] + ind - i
                    val = max(dp(i),tmp)
                    count = max(count,val)
                dpvalue[ind] = count

            return dpvalue[ind]

        return dp(0)            



                 








        print(value) 

        return 0