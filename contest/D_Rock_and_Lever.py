from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))


    freq = defaultdict(int)
    ans = 0
    for i in range(len(arr)):
        num = arr[i].bit_length()
        if num in freq:
            ans += freq[num]
        freq[num]+=1
    print(ans)