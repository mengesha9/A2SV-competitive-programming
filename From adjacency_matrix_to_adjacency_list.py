n = int(input())


for i in range(n):
    row = list(map(int,input().split()))
    arr = []
    for j in range(len(row)):
        if row[j]==1:
            arr.append(j+1)
    print(len(arr),end=" ")
    print(*arr)        
            

    
