class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        arr=[]
        size=len(arr)
        for i in range(len(pushed)):
            arr.append(pushed[i])
            j=0
            while  size!=0 and arr[-1]==popoed[j]:
                arr.pop()
                j+=1
        return True if size ==0 else False
