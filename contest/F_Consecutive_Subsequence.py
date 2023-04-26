from collections import defaultdict
freq = defaultdict(int)

n = int(input())
arr = list(map(int,input().split()))

j = len(arr)-1
while j>=0:
    if arr[j]+1 in freq:
        freq[arr[j]+1].append(j+1)
        freq[arr[j]]=freq[arr[j]+1]
    else:
        freq[arr[j]] = [j+1]
    j-=1

y = max(freq)
print(len(y))
print(*y[::-1])
