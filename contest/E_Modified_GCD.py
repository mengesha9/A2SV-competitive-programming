import bisect
import math


def commondivider(a, b):
    right = math.gcd(a,b)
    left = right//2
    arr = []
    for i in range(1, left):
        if right % i == 0:
            arr.append(i)
    for i in range(left,right+1):
        if right % i == 0:
            arr.append(i)        
        

    
    return arr


a, b = map(int, input().split())

n = int(input())
result = commondivider(a, b)
for _ in range(n):
    low, high = map(int, input().split())

    # left = bisect.bisect_left(result, low)
    right = bisect.bisect_right(result, high)-1
    ans = result[right]
    if low > ans:
        print(-1)
    else:
        print(ans)


