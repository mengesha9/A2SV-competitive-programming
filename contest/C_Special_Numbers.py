
def findbits(n,k):
    res = 0
    x = 0
    while k:
        if k % 2 != 0:
            res += n**(x)
        x += 1
        k >>=1
    return res  

t = int(input())
mod = (10**9) + 7
for _ in range(t):
    n,k = map(int,input().split())
    ans = findbits(n,k)

    print(ans % mod)    

