test_case=int(input())
for t in range(test_case):
    a,b=map(int,input().split())
 
    min_value=min(a,b)
    temp=(a+b)//4
    res=min(min_value,temp)
    print(res)
