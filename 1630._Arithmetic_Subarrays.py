class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:


        answer=[]
        for i in range(len(l)):
            total=nums[l[i]:r[i]+1]
            total.sort()
            if len(total)==2:
                answer.append(True)
            else:    
                for j in range(1,len(total)-1):
                    # if len(total)==2:
                    #     ans=True
                    #     break
                    if total[j]-total[j-1]!=total[j+1]-total[j]:
                        ans=False
                        break
                    ans=True
                answer.append(ans)
        return answer  
