n = int(input())
l = [0]*(n+1)
for i in range(2,n+1):
    if l[i] == 0:
        for j in range(2*i, n+1,i):
            l[j] += 1

print(l.count(2))
    