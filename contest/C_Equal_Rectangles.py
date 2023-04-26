from collections import defaultdict
q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    freq = defaultdict(int)
    i = 0
    j = len(arr)-1
    while j > 0  and i < len(arr):
        freq[arr[i] * arr[j]]=1
        i += 1
        j -= 1

    if len(freq) == 1 and arr[::2] == arr[1::2]:
        print("YES")
    else:
        print("NO")
