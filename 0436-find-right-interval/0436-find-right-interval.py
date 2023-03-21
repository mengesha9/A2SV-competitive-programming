class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        end = []
        start = []
        index = defaultdict(int)

        for i in range(len(intervals)):
            end.append(intervals[i][1])
            start.append(intervals[i][0])
            index[intervals[i][0]] = i
       
        start.sort()
         
        arr = []
        for i in range(len(end)):
            temp = bisect_left(start,end[i])    

            if temp == len(start):
                arr.append(-1)
            else:
                arr.append(index[start[temp]])

        return arr        




        




        