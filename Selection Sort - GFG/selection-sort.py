#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
            j += 1
        return minIndex    
            
            
    
    def selectionSort(self, arr,n):
        
        #code here
        
        for i in range(n):
            tmp = self.select(arr,i)
            arr[i],arr[tmp] = arr[tmp],arr[i]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends