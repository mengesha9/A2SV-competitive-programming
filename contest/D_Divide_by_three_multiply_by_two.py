
n = int(input())
ouptput = list(map(int, input().split()))

def multiply(n):
    i = 0
    while n % 2 == 0:
        i += 1
        n /= 2
    return (-n, i)


ouptput.sort(key=multiply)
print(*ouptput)

