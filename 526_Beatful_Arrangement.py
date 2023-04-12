class Solution:
    def countArrangement(self, n: int) -> int:

        result = []
        self.total = 0
        visited = set()
        tmp = [i+1 for i in range(n)]
        
        def dfs(arr):
            if arr:
                if arr[-1] % len(arr) != 0 and len(arr)% arr[-1] != 0:
                    return False
            if len(arr) == n :
                if arr[-1] % len(arr) == 0 or len(arr)% arr[-1] == 0:
                    self.total += 1
                    return 
            
            for i in range(n):
                if tmp[i] not in visited:
                    arr.append(tmp[i])
                    visited.add(tmp[i])
                    dfs(arr)
                    arr.pop()
                    visited.remove(tmp[i])

        dfs([])
       

        return self.total           
                     


        