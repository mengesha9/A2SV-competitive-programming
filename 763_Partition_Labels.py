class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        d={}
        for i in range(len(s)):
                d[s[i]]=i
        print(d) 
        i=0
        j=0
        index=0
        result=[]
        while j<len(s):
            index=max(d[s[j]],index) 
            if j==index  :
                result.append(j-i+1)
                if len(s)-j>=2:
                    i=j+1
                else:
                    i=j        
            j+=1
        return result   
