class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        self.parent = [x for x in range(len(edges)+1)]

        def connect (x,y):
            node1 = rep(x)
            node2 = rep(y)
            self.parent[node1]=node2

        def rep(x):
            while x != self.parent[x]:
                x = self.parent[x]
            return x 

        for u,v in edges:
            if rep(u)==rep(v):
                return [u,v]
            else:
                connect(u,v)