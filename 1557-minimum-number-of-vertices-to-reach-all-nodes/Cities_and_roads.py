n = int(input())
arr = []
for _ in range(n):
    li = list(map(int,input().split()))
    arr.append(li)
visit = set()
road = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if (j,i) not in visit and arr[i][j] == 1:
            road += 1
            visit.add((i,j))

print(road)           
