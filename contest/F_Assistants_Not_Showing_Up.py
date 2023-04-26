n, m = map(int,input().split())
arr = [-1]*n
count = n

for _ in range(m):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        if arr[i] == -1:
            arr[i] = i
            count -= 1
        
print("YES") if count > 0 else print("NO")
