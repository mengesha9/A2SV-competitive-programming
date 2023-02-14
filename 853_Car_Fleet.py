class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        arr=[]
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            arr.append([position[i],time])
        print(arr)  
        arr.sort()
        print(arr)
        stack=[] 
      
        arr=arr[::-1]
        for i in range(len(arr)):
            
            if  not stack or (stack and stack[-1]<arr[i][1]):
                stack.append(arr[i][1])
            
        return len(stack)        




       
