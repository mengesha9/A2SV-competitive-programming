n,k=map(int,input().split())
students=list(map(int,input().split()))
students.sort()
ans=0
left=0
right=len(students)-1
while k > 0:
    mid=left+(right-left)//2
    ans+=min(k,mid-left+1)*students[mid]
    k-=min(k,mid-left+1)
    left=mid+1
print(ans)   


