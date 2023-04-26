n, v =  map(int,input().split())


tank = v
const = v
for i in range(n+1):

    tank -=1
    if n-i > tank :
        tank += (v-tank)
        const += (v-tank)*i
print(n-1) if v >= n-1 else print(const)






