n, start, end = map(int,input().split())
solved = list(map(int, input().split()))


def helper(arr,target):
    _sum=left=0
    count=0
    for i in range(len(arr)):
        _sum+=arr[i]
        while _sum>=target:
            _sum-=arr[left]
            left+=1
        count+=i-left+1
    return count 

print(helper(solved,end+1)-helper(solved,start))


