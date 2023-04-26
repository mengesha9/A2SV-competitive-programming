from collections import defaultdict
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    total = 0

    arr.sort()
    i = 0
    while i < len(arr) and  arr[i] <= x :
        total += arr[i]
        i += 1

    totalsum = (x*(x+1))//2
    print(totalsum - (2*total))
