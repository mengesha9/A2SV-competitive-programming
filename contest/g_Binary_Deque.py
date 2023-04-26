test = int(input())

for _ in range(test):
    n, s = map(int,input().split())
    arr = list(map(int,input().split()))
    
    
    left = right =total = 0
    ans = 0
    while right<n :
        total += arr[right]
        
        while left < n and total > s:
            total -= arr[left]
            left += 1
        if total == s:
            ans = max(ans, right-left+1)
    
        right += 1
    print(len(arr)-ans)  if sum(arr) >= s else print(-1)  
    







    

