class Union:
    def __init__(self,str1):
        self.parent = { n:n for n in str1 }
        # self.rank ={ n:1 for n in str1}
        self.componnets = len(str1)
    def find(self,value):
        if self.parent[value] == value:
            return value
        ans = self.find(self.parent[value])
        self.parent[value] = ans
        return ans 
    def connect(self,s1,s2):
        x = self.find(s1)
        y = self.find(s2)
        if x  != y :
            
            self.parent[x] = y
            self.componnets -= 1     
            
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(a,b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                if count > 2:
                    return False 
            return True             


        union = Union(set(strs))


        for i in range(1, len(strs)):
            for j in range(i):
                if check(strs[i],strs[j]):
                    union.connect(strs[i],strs[j])


        return union.componnets             
        
