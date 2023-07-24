class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.dead = set()
        self.king = kingName
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        
        order = []
        if self.king not in self.dead:
            order.append(self.king)
        def dfs(node):
            if node not in self.graph:
                return 
            for n in self.graph[node]:
                if n not in self.dead:
                    order.append(n)
                if n in self.graph:    
                    dfs(n)  

        dfs(self.king)

        return order 

                




        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()