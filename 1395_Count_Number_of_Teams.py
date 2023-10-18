class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n, count = len(rating),0
        for i in range(len(rating)):
            s_left = 0
            g_left = 0
            s_right = 0
            g_right = 0

            for j in range(i):
                if rating[j] > rating[i]:
                    g_left += 1
                if rating[j] < rating[i]:
                    s_left += 1

            for k in range(i+1,n): 
                if rating[k] > rating[i]:
                    g_right += 1
                if rating[k] < rating[i]:
                    s_right += 1
            count += s_left * g_right + s_right*g_left

        return count             

       
    


                        
                    


                



        
