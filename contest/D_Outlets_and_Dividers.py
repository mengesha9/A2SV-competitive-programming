test=int(input())
for _ in range(test):
    n, m = map(int, input().split())
    num=list(map(int,input().split()))
    total_outlet = 2
    num.sort()
    no_diveder=0
    j=len(num)-1
    while total_outlet < n and j >= 0 and n > 2:
        total_outlet += (num[j]-1)
        no_diveder += 1
        j-=1

    print(no_diveder) if total_outlet>=n else print(-1)



