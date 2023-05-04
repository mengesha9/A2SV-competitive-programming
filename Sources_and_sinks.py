from collections import defaultdict
n = int(input())
di = defaultdict(list)
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j]==1:
            di[i+1].append(j+1)
            
sink = [-1]*n
source = [-1]*n
for k,v in di.items():
    source[k-1]=1
    for i in v:
    
        sink[i-1]=1
arr = []
si = []
for i in range(len(source)):
    if source[i]==sink[i]==-1:
        arr.append(i+1)
        si.append(i+1)
    
    elif source[i]==sink[i]==1:
        continue
    elif source[i]==1 and sink[i]==-1:
        arr.append(i+1)
    elif source[i]==-1 and sink[i]==1:
        si.append(i+1)   



print(len(arr),end=" ")
print(*arr)
print(len(si),end=" ")
print(*si)
