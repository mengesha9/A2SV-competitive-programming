class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:


        def small(string):
            smallString =  string[0]
            dic = defaultdict(int)
            
            for char in string:
                dic[char] += 1
                if char < smallString:
                    smallString = char 


            return  dic[smallString]


        arr = []
        
        for w in words:
            num = small(w)
            arr.append(num)

        arr.sort() 

        answer = []
        for q in  queries:
            num = small(q)
            tmp = bisect_right(arr,num)
            answer.append(len(arr)-tmp)

        return answer