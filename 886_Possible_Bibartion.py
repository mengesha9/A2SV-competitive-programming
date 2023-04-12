class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        if len(dislikes)<=1:
            return True

        self.graph = defaultdict(set)
        self.visit= set()

        for edge in dislikes:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])
        self.one= set()
        self.zero = set()
        def dfs(k,color):
            if ( color == 0 and k in self.one) or (color == 1 and k in self.zero):
                return False
            elif( color == 0 and k in self.zero) or (color == 1 and k in self.one):
                return True
            if color == 0:
                self.zero.add(k)
            else:  
                self.one.add(k) 
            count = True  
            self.visit.add(k)         
            for i in self.graph[k]:
                count &= dfs(i,1^color)   
            return count          

        count = True
        for k,v in self.graph.items():
            if k not in self.visit:
                count &=  dfs(k,0)
        return count         




    

                





            

        
            



