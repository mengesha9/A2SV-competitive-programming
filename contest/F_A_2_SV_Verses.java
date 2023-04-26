n,a,b=int(input())
solved=list(map(int,input().split()))

count=0
res=0
i=0
j=0
while i<=j and j<len(solved):
    
    if a<=count<=b:
        while  a<=count<=b and i<len(solved):
            res+=1
            count-=solved[i]
            i+=1
    elif count<a:
        count += solved[j]
        j+=1 
    elif count>b:
        count-=solved[i]
        i+=1
print(res)        



