class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:


        self.graph = defaultdict(int)

        self.result = []
        self.n = 0
        for i in range(len(graph)):
            self.graph[i]= graph[i]
            if graph[i]:

                self.n = max(self.n,max(graph[i]))
        
        def dfs(k,arr):

            if k == self.n:
                self.result.append(arr.copy())
                return 


            for i in self.graph[k]:

                arr.append(i)
                dfs(i,arr)
                arr.pop()

        dfs(0,[0])

        return self.result 




    


