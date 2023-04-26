from collections import defaultdict

test = int(input())
for _ in range(test):

    n,m = map(int,input().split())
    hash_pos = defaultdict(int)
    hash_neg = defaultdict(int)
    arr = []

    for i in range(n):
        newval = list(map(int,input().split()))
        for j in range(m):
            
            
            hash_pos[i+j] += newval[j]
            hash_neg[i-j] += newval[j]
            
        arr.append(newval) 

    total = 0 
    for i in range(n):
        for j in range(m):
            newtotal = hash_pos[i+j] + hash_neg[i-j] - arr[i][j]
            total = max(total,newtotal )

    print(total)        



