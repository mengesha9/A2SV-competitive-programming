n,k = map(int,input().split())
arr = list(map(int,input().split()))

def merge(arr,s,e):

    if s==e:
        return [[arr[s],s]]
    mid = s + (e-s)//2
    left = merge(arr,s,mid)
    right = merge(arr,mid+1,e)

    ans = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] >= right[j][0] : 
            if left[i][0] -right[j][0] <= k: 
                ans.append(right[j])
            j += 1
        else:
            if right[j][0] - left[i][0] <=k:
                ans.append(left[i]) 
            i += 1 

    while i < len(left):
        ans.append(left[i])
        i += 1

    while j < len(right):
        ans.append(right[j]) 
        j += 1  
    
    return ans



output = merge(arr,0,len(arr)-1)
res = []
for i in range(len(output)):
    res.append(output[i][1]+1)

res.sort()
print(*res)


















