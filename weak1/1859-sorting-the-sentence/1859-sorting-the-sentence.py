class Solution:
    def sortSentence(self, s: str) -> str:
        ar = s.split(" ")
        ar.sort(key = lambda x : x[-1])
        
        st = ""
        
        for s in ar:
            st += (s[:len(s)-1])
            st += " "
        
        
        return st[:len(st) - 1]