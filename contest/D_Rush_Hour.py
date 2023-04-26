import math
n,m=map(int,input().split())

x=[int(input()) for i in range(n)]
# for i in range(n):
#     arr[i]=int(input())
sumx=0    
for i in range(len(x)):  
    sumx+=x[i]  
result=math.ceil(sumx/m)
print(result)