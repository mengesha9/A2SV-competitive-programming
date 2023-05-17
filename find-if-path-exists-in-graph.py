class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        self.parent=[x for x in range(n)]

        def connect(x,y):
            node1 = representative(x)
          
            node2 = representative(y)
            self.parent[node1] = node2
            

        def representative(num):
            while self.parent[num]!=num:
                num= self.parent[num]
            return num 

        for u,v in edges:
            connect(u,v)

        return   representative(source) == representative(destination)