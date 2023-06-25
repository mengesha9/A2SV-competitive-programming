class Solution:
    def maxLength(self, arr: List[str]) -> int:


        self.ans = 0
        n = len(arr)
        def back(ind,string):
            if string :
                self.ans = max(self.ans,len(string))
            if ind == n:
                return     
            tmp = string
            for i in range(ind,n):

                tmp = string + arr[i]
                used = set(tmp)

                if len(used) == len(tmp):
                    back(i+1,tmp)

                tmp = string 

        back(0,'')

        return self.ans