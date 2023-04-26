from collections import defaultdict
test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    k = sum(arr)/n
    target_sum = sum(arr) - k*(n-2)

    freq = defaultdict(int)
    count = 0  
    for i in range(n):
        diff = target_sum -arr [i]
        if diff in freq:
            count += freq[diff]
        freq[arr[i]]+=1 
    print(count)       