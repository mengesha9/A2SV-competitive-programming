class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

class Trie :
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            ind = ord(word[i]) - ord('a')
            
            if not node.children[ind] and i == len(word)-1:
                node.children[ind] = TrieNode()
                
            elif not node.children[ind] and i < len(word)-1:
                return False 
            
            node = node.children[ind]    

        return True 

class Solution:
    def longestWord(self, words: List[str]) -> str:

        words.sort()
        trie = Trie()
        res = ''
        for word in words:
            arr = []
            if trie.insert(word):
                if len(res) < len(word):
                    res = word
                elif len(res) == len(word) and word < res:
                    
                    res = word
        
        return res