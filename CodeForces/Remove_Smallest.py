t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    i = 0
    j = 1
    dic = set()
    while j < len(arr):
        if abs(arr[i]-arr[j])<=1:
            dic.add(i)
        i += 1
        j += 1 
    
    print("YES") if len(dic)+1 == len(arr) else print("NO")
