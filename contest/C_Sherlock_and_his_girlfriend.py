n = int(input())

def isprime(n):
    d= 2
    arr = []
    while d*d <= n:
        while n % d == 0:
            return False
        d += 1
    
    return True   

color = []          
for i in range(2,n+2):
    if isprime(i):
        color.append(1)
    else:
        color.append(2)

print(len(set(color))) 
print(*color)           




