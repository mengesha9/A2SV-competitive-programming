n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

i = 0
j = 0
ans = []
while i < len(arr2):
    while j < len(arr1) and arr2[i]>arr1[j]:
        j += 1
    ans.append(j)
    i += 1   
while i < len(arr2):
    ans.append(j)

print(*ans)

