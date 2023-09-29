class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.freq = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for n in word:
            ind = ord(n) - ord('a') 
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
                
            curr  = curr.children[ind]
            curr.freq += 1

    def findScore (self, word):
        score = 0
        curr = self.root
        
        for n in word:
            ind = ord(n) - ord('a')
            if not curr.children[ind]:
                return score 
            curr = curr.children[ind]
            score += curr.freq
            
        return score     


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
       
        arr = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:

            res = trie.findScore(word)
            arr.append(res)

        return arr