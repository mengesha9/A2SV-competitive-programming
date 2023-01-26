class Solution:
    def numRabbits(self, answers: List[int]) -> int:




        dic={}
        num=0
        for i in range(len(answers)):
            newrabit=answers[i]+1
            if newrabit in dic:
               
                if dic[newrabit]>=newrabit:
                    dic[newrabit]=1
                    num+=newrabit
                else:
                    dic[newrabit]+=1  
            else:
                dic[newrabit]=1 
                num+=newrabit
        return num             








