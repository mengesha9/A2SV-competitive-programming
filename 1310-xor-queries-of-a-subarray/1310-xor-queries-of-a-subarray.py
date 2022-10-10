class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        preFix=[0]*(len(arr)+1)
        answer=[]
        for i in range(len(arr)):
            preFix[i+1]=preFix[i]^arr[i]
            
        for l , r in queries :
            answer.append(preFix[r+1]^preFix[l])
        return answer 
        