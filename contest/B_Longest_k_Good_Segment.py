from collections import defaultdict
n, k = map(int,input().split())

arr = list(map(int,input().split()))
freq =  {}
i = j = size = left = right = 0

while j < len(arr):

    while  i < len(arr) and len(freq.values()) >= k:
        if size <= j-i + 1:
            left = i
            right = j
            size = j-i+1
        freq[arr[i]]-=1
        if freq[arr[i]] == 0:
            del freq[arr[i]]
        i += 1 
    if arr[j] in freq:
        freq[arr[j]] += 1
    else:
        freq[arr[j]] = 1
    j += 1    

print ( " {} {} ".format(left, right))

    


