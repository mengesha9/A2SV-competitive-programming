def mergesort(l,r, arr):
    if l >= r:
        return [arr[l]] , 0
    mid = l + (r-l)//2
    left , countleft = mergesort(l, mid,arr)
    right , countright= mergesort(mid+1,r,arr)

    if left[0] > right[0]:
    
        return right + left, countright + countleft + 1
    else:
        return left + right, countleft + countright
    
test = int(input())
for _ in range(test):
    n = int(input())
    num = list(map(int,input().split()))
    arr, res = mergesort(0, len(num)-1, num)
    flag = True
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            flag = False
            break
    if flag:
        print(res)  
    else:
        print(-1)
