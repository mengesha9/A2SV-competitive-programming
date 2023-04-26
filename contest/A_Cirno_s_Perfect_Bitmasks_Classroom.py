test = int(input())
for _ in range(test):

    x = int(input())

    y = 0
    k = 0

    while (x % 2) == 0:
        k += 1
        x >> 1
    
    y += 2**(k)

    if (x >> 1) % 2 == 0:
        y += 2**(k+1)
    
    print(bin(5))    
        