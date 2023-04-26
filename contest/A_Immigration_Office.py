n=int(input())
names=list(input().split())
test=int(input())
for _ in range(test):
    name=input()
    
    best=len(names)
    right=len(names)-1
    left=0
    while left<=right:
        mid=left+(right-left)//2
        if names[mid]<name:
            left=mid+1
        else:
            best=mid
            right=mid-1
    print(best)        



