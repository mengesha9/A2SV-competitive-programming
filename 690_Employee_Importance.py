"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:


 
        self.Id = defaultdict(int)
        self.sub = defaultdict(int)

        for employ in employees:
            self.Id[employ.id] = employ.importance
            self.sub[employ.id] = employ.subordinates


        def dfs(i):
            if len(self.sub[i]) == 0:
                return self.Id[i]   

            count = self.Id[i]
            for sr in self.sub[i]: 
                count += dfs(sr)

            return count 


        return dfs(id)        







      