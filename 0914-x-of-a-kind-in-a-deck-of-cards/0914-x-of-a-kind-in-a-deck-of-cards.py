class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        

        di = defaultdict(int)
        for i in range(len(deck)):
            di[deck[i]] += 1

        part = min(di.values())
        if part < 2:
            return False
        arr = []    
        deck = list(set(deck))
        for i in range(2,part+1) :
            tmp = i
            hasfound = True
            for j in range(len(deck)):
                if di[deck[j]] % tmp != 0:
                    hasfound = False
                    break
            if  hasfound:
                return True
                 

        return False        

       