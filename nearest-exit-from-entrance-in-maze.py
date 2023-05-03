class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        q = deque()
        q.append([0,entrance[0],entrance[1]])
        visit = set()
        visit.add((entrance[0],entrance[1]))
        while q :
            step,r,c= q.popleft()
            if step > 0 and (r==0 or r==n-1 or c==0 or c==m-1) :
                return step
            di = [[1,0],[-1,0],[0,1],[0,-1]]   
            for sr,sc in di:
                row = sr+r
                col = sc+c
                if min(row,col)>=0 and row<n and col < m and maze[row][col]!="+" and (row,col) not in visit:
                    q.append([step+1,row,col])
                    visit.add((row,col))
        return -1