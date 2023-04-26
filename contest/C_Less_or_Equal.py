n, k = map(int, input().split())
arr = [1] + sorted(list(map(int, input().split())))

if n == k or  arr[k+1] > arr[k] :
    print(arr[k])
else:
    print(-1)


