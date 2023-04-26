from collections import defaultdict
test = int(input())

for _ in range(test):
    n,k = map(int,input().split())
    string = input()
    freq = defaultdict(int)
    for i in range(n):
        freq[string[i]] += 1
    arr = list(freq.keys())   
    i = 0 
    print(arr)
    # while    

