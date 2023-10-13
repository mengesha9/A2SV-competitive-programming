class Solution:
    def knightDialer(self, n: int) -> int:

        mod = 10**9 + 7
        arr = [[0]*3 for i in range(4)]
        count = 1
        for i in range(3):
            for j in range(3):
                arr[i][j] = count 
                count += 1
   
        arr[-1][0] = "*"
        arr[-1][1] = 0
        arr[-1][2] = "#"  
        print(arr)      
        di = [[-1,2],[1,2],[-1,-2],[1,-2],[-2,-1],[-2,1],[2,-1],[2,1]]
        dp = {}
        def dfs(r,c,total):
            if total == 1:
                return 1
            if (r,c,total)  not in dp:   
                val = 0
                for sr,sc in di:
                    row = sr+r
                    col = sc+c
                    if min(row,col) >= 0 and row < 4 and col < 3 and arr[row][col] != "#" and arr[row][col] != "*":

                        val += dfs(row,col,total-1)
                        
                dp[(r,c,total)] = val

            return dp[(r,c,total)] % mod

        ans = 0
        for i in range(4):
            for j in range(3):
                if arr[i][j] != "*" and arr[i][j] != "#":
                    ans += dfs(i,j,n)

        return ans  % mod           

 

        
