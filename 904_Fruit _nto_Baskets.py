class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i=0
        j=0
        arr=[]
        res=0
        count={}
        while j<len(fruits):
            count[fruits[j]]=j
            if len(count)>=3:
                minindex=min(count.values())
                del count[fruits[minindex]]
                i=minindex+1
            res=max(res,j-i+1) 
            j+=1
        return res 
