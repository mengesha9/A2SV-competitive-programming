class Solution:
    def racecar(self, target: int) -> int:

      
        visit = set()

        q = deque()
        q.append((0,1,0))

        while q:
            p, s, leng = q.popleft()  

            if p == target:
                return leng
            if s > 0:
                if (p,-1) not in visit:
                    q.append((p,-1,leng+1))
                    visit.add((p,-1))
                if (p+s , s*2)  not in visit:
                    q.append((p+s,s*2,leng+1))
                    visit.add((p+s , s*2))
            if s < 0:
                if (p+s,s*2) not in visit:
                    q.append((p+s,s*2,leng+1))
                    visit.add((p+s,s*2))

                if (p,1) not in visit:
                    q.append((p,1,leng+1))
                    visit.add((p,1))