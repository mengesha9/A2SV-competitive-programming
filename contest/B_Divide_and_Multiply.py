
def findsum(i,arr):
    for j in range(len(arr)):
        while i != j and arr[j]%2 ==0:
            arr[j]//=2
            arr[i]*=2        

    return sum(arr)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxsum = 0
    for i in range(len(arr)):
        maxsum = max(maxsum, findsum(i,arr))

    print(maxsum)    
