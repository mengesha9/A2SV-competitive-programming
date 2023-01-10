class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:


        presum=[0]*len(chalk)
        presum[0]=chalk[0]
        for i in range(1,len(chalk)):
            presum[i]=presum[i-1]+chalk[i]
        r=k%presum[-1]  
        
        if r== 0:
            return 0
        for i in range(len(chalk)):
            r-=chalk[i]
            if r<0:
                return i
          
