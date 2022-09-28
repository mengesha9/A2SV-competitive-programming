class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count=0
        dic={}
        for x in nums:
            diff=k-x
            if diff in dic and dic[diff]>0:
                count+=1
                dic[diff]-=1
            else:
                if x not in dic:
                    dic[x]=0
                dic[x]+=1
        return count
