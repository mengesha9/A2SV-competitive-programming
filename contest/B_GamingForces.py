test = int(input())
for _ in range(test):
    n  = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    i = 0
    count = 0
    while i< len(arr):
        if i+1 < len(arr)  and arr[i] + arr[i+1] <= 2  :
            i += 2
        else:
            i += 1 
        count += 1  
    print(count)     

