class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        dicts=defaultdict(int) 
        dictp=defaultdict(int)  
        if len(p)>len(s):
            return []
        for i in range(len(p)) :
            dictp[p[i]]+=1
            dicts[s[i]]+=1
        count=[]
        if dictp==dicts:
            count.append(0)
        i=1
        j=len(p)
        while   j<len(s):
            
            dicts[s[i-1]]-=1
            if dicts[s[i-1]]==0:
                del dicts[s[i-1]]
            dicts[s[j]]+=1 
            if dicts==dictp:
                count.append(i)
            i+=1
            j+=1
        return count           
             

            





       
        

                


