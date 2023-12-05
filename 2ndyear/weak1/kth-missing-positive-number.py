class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        n=len(arr)
        arr2=[]
        for i in range(k+n):
            if (i+1) not in arr:
                arr2.append(i+1)
        print(arr2)  
        return arr2[k-1]      


                

