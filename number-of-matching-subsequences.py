class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None for _ in range(26)]
        self.freq = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root

        for n in word:
            ind  = ord(n) - ord('a')
            if not node.children[ind]:
                node.children[ind] = TrieNode()
            node = node.children[ind]

        node.isEnd = True
        node.freq += 1

    def numberOfmatch(self, word):

        def dfs(curr , ind):

            count = 0
            if curr.isEnd:
                count += curr.freq    

            for i in range(26):
    
                if curr.children[i] :
                    w = chr(i+97)
                    index = word.find(w,ind)
                    if index != -1:
                        count += dfs(curr.children[i],index+1)

            return count 

        return dfs(self.root,0 )


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        trie = Trie()

        for word in words:
            trie.insert(word)

        return trie.numberOfmatch(s)