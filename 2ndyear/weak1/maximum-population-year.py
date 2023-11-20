class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        arr = [0]*101

        for v,u in logs:
            arr[v-1950] += 1
            arr[u-1950] -= 1
        total= 0 
        max_val =0 
        max_year = 0  
        for i in range(len(arr)):
            total += arr[i]
            if max_val < total:
                max_year = i
                max_val = total

        return 1950 + max_year 
                


    



    


        