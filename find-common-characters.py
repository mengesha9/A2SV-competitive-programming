class Solution:
    def commonChars(self, words: List[str]) -> List[str]:


        tmp = set(words[0])
        arr = list(tmp)

        dic = defaultdict(list)

        for i in range(len(words)):
            for w in arr:
                dic[w].append(words[i].count(w))

     
        ans = []
        for x in arr:
            ind = min(dic[x])
            while ind>0:
                ans.append(x)
                ind -= 1

        
        return ans