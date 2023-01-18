class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        stack=[]
        answer=[0]*len(temperatures)
        i=0
        while i<len(temperatures):
            while stack and stack[-1][0]<temperatures[i]:
                x,y=stack.pop()
                answer[y]=i-y
            stack.append([temperatures[i],i])
            answer[i]=0
            i+=1
        return answer    
