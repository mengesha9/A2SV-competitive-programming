class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        obj = union()
        for e in equations:
            if e[1] == '=':
                obj.connect(e[0], e[3])

        for e in equations:
            if e[1] == '!' and obj.find(e[0]) == obj.find(e[3]):
                return False 

        return True         


class union:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connect(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y