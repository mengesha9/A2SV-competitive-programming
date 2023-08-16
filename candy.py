class Solution:
    def candy(self, ratings: List[int]) -> int:

        arr = [1]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr.append(arr[-1]+1)
            elif ratings[i] == ratings[i-1]:
                arr.append(1)
            elif ratings[i] < ratings[i-1]:    
                if arr[-1] == 1:
                    arr[-1] += 1
                arr.append(1)
        
        for i in range(len(arr)-2,-1,-1):
            
            if ratings[i] > ratings[i+1] and  arr[i] <= arr[i+1]:
                arr[i] += ( arr[i+1]-arr[i] + 1)

        return sum(arr)