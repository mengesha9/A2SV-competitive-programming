class Solution:

    def distribute(self, i, cookies ,bucket):
        if i >= len(cookies):
            return  max(bucket)
        answer = float('inf')
        for j in range(len(bucket)):
            bucket[j] += cookies[i]
            if bucket[j] < answer:
                answer = min (answer , self.distribute(i+1, cookies , bucket))
            bucket[j] -= cookies[i]

        return   answer  
        
        
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        cookies.sort(reverse = True)
        bucket = [ 0 for i in range(k)]
    
        return self.distribute(0, cookies, bucket )

         



            


    




