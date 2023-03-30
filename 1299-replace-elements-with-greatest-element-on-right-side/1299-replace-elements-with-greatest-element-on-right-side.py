class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greval = arr[-1]
        i = len(arr)-2
        arr[-1] = -1
        while i>=0:
            tmp =arr[i]
            arr[i]= greval
            greval = max(greval, tmp)

            i -= 1
        return arr    




