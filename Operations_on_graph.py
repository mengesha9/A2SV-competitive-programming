from collections import defaultdict
n = int(input())
k = int(input())
graph = defaultdict(list)
for i in range(k):
    arr = list(map(int,input().split()))
    if len(arr) == 2:
        print(*graph[arr[1]])
    elif len(arr) == 3:
        graph[arr[1]].append(arr[2])
        graph[arr[2]].append(arr[1])
