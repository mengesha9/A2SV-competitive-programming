import  bisect
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
for _ in range(n):
    di = int(input())
    ind = bisect.bisect_left(arr,di)
    if m-ind != m and (m-ind) > m//2:
        print("YES")
    else:
        print("NO")    

