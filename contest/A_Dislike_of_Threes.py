t = int(input())
for _ in range(t):
    k = int(input())
    count = 0
    i = 1
    tmp = k
    while k>0:
        if i % 3 == 0:
            i += 1
            count += 1
           
        k -= 1
    print(count + tmp)        

        
    