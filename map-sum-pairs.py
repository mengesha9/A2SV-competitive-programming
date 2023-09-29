class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = [None for _ in range(26)]

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.visit =  defaultdict()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        hasfound = False 
        value = 0
        if key in self.visit:
            hasfound = True
            value = self.visit[key]

        self.visit[key] = val


        for n in key:
            ind = ord(n) - ord('a')
            if  not  node.children[ind]:
                node.children[ind] = TrieNode()

            node = node.children[ind]
            if hasfound:
                node.count += (val-value)
            else:
                node.count += val    
        
        
    def sum(self, prefix: str) -> int:
        node = self.root
        for n in prefix:
            ind = ord(n) - ord('a')
            if not node.children[ind]:
                return 0
            node = node.children[ind] 

        return node.count
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)