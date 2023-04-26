from collections import defaultdict
n,m = map(int,input().split())
arr = list(map(int,input().split()))
freq = defaultdict(list)
for _ in range(n-1):
    parent ,node = map(int,input().split())
    freq[parent].append(node)


def dfs(node,count):
    if count == m and arr[node] == 1:
        return 0
    if not freq[node] and count < m:
        return 1
    ans = 0
    for k in freq[node]:
        if arr[k-1] == 1:
            ans += dfs(k,count + 1) 
        else:
            ans += dfs(k,count) 
    return ans 
print(dfs(1,0))



