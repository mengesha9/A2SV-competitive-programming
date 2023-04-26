def countSecond(arr, mid):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] + mid < arr[i+1]:
            count += mid
        else:
            count += arr[i+1]-arr[i]
    count += mid
    return count


t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 1
    right = h
    best = h
    while left <= right:
        mid = left + (right-left)//2
        if countSecond(arr, mid) >= h:
            best = mid
            right = mid - 1
        else:
            left = mid + 1
    print(best)
