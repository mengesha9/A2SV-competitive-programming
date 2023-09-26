class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            ind = ord(ch) - ord("a")

            if not curr.children[ind]:
                curr.children[ind] = Trie()
            curr = curr.children[ind]

        curr.is_end = True     

    def search(self, word: str) -> bool:
        def dfs(curr,ind):
            if ind >= len(word):
                return curr.is_end
            if word[ind] == '.':
                for i in range(26):
                    if curr.children[i] and  dfs(curr.children[i],ind+1):
                            return True
                return False
            else:
                i = ord(word[ind]) - ord('a')
                if not curr.children[i]:
                    return False 
                return dfs(curr.children[i],ind + 1) 


        return dfs(self.root,0)     


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)