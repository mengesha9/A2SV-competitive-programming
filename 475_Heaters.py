class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        dic = defaultdict(int)
        for n in heaters:
            dic[n] += 1
           
        def find(a,b):

            ind1 = bisect_left(heaters,a)
            ind2 = bisect_right(heaters, b)

            if ind1 == ind2:
                return False 
            else:
                return True      

        def binary(rad):
            for n in houses:
                if n not in dic and  not find(n-rad, n+rad):
                    return False   
            return True

        left = 0
        right = 10**9
        best = right

        while left <= right:
            mid = (left+right)//2
            if binary(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1 

        return best           

        
