from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        obj = UnionFind(s1, s2)
        ans = ''
        
        for n in baseStr:
            ans += obj.findRoot(n)
        
        return ans


class UnionFind:
    def __init__(self, s1, s2):
        self.parent = {}
        
        for c1, c2 in zip(s1, s2):
            self.union(c1, c2)
    
    def findRoot(self, x):
        if x not in self.parent:
            return x
        root = self.findRoot(self.parent[x])
        self.parent[x] = root  
        return root
    
    def union(self, x, y):
        root_x = self.findRoot(x)
        root_y = self.findRoot(y)
        
        if root_x != root_y:
            if root_x < root_y:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y