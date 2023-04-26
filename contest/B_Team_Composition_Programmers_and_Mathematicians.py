test_case=int(input())
for t in range(test_case):
    a,b=map(int,input().split())

    # min_value=min(a,b)
    # temp=(a+b)//4
    # res=min(min_value,temp)
    # print(res)

    y=min(a,b)
    x=max(a,b)

    if (a==0 or b==0) or (a+b)<4 :
        print(0)
    else:
        def helper(c, d):
            y1 = y//c
            x2 = x//d
            return min(y1, x2)
        i=1
        team=0   
        while i<=3 and i<=y:
            team=max(team,helper(i,4-i))
            i +=1
        print(team)   
        






