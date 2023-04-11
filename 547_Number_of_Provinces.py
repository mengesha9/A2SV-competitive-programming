class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected) 
        self.graph = defaultdict(set)
        self.visit = set()
                
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] != 0 :

                    
                    self.graph[i+1].add(j+1)
                    
                    self.graph[j+1].add(i+1)

        def dfs(k):
            if k in self.visit:
                return 0
            self.visit.add(k)
            count = 0
            for i in self.graph[k]:
                count += dfs(i)   
            return   count               

        count = 0
        for k,v in self.graph.items():
            if k not in self.visit:
                count += 1
                dfs(k)

        return count         



        




          








       


      



               



            
                
        