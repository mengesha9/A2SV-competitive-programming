class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1)>len(s2):
            return False
        dicts1=defaultdict(int)
        dicts2=defaultdict(int)
        for i in range(len(s1)):
            dicts1[s1[i]]+=1
            dicts2[s2[i]]+=1

        if dicts1 ==dicts2:
            return True
        i=0
        j=len(s1) 
        while j<len(s2):

            dicts2[s2[i]] -= 1
            if dicts2[s2[i]]==0:
                del dicts2[s2[i]] 

            dicts2[s2[j]] += 1
            if dicts1 == dicts2:
                return True
            i+=1
            j+=1
        return False            
