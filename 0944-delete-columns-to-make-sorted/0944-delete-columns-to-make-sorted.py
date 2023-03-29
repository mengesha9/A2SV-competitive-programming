class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        for i in range(len(strs[0])):
            j = 0
            issorted = False
            while j < len( strs)-1:
                if strs[j][i] > strs[j+1][i]:
                    issorted = True
                    break
                j += 1    
            if  issorted:
                count += 1

        return count         



        