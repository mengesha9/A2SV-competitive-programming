n, m = map(int, input().split())

def uniqe(r,c):
    foundr = True
    foundc = True
    for i in range(m):
        if c != i and arr[r][c] == arr[r][i]:
            foundr = False
    for i in range(n): 
        if r != i and arr[i][c] == arr[r][c]:
            foundc = False
    return foundr and foundc


arr = []
for _ in range(n):
    arr.append(input())

count = ''
for i in range(n):
    for j in range(m):
        if  uniqe(i,j):
            count += arr[i][j]

print(count)


