class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[[0,0,0] for i in range(len(points))]
        ansewr=[]
        for i  in range(len(points)):
            dist[i][0]=points[i][0]
            dist[i][1]=points[i][1]
            dist[i][2]=(points[i][0]**2)+(points[i][1]**2)
        dist.sort(key=lambda x:x[2])
        for i in range(k):
            ansewr.append([dist[i][0],dist[i][1]])
        return ansewr    
