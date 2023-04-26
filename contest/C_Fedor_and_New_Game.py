n,m,k = map(int,input().split())
arr = []
for _ in range(m+1):
    arr.append(int(input()))



def findbit(bit,fedor):
    dif = 0
    while bit >0 or fedor >0 :
        if (bit % 2 == 0 and fedor % 2 != 0) or (bit % 2 != 0 and fedor % 2 == 0):
            dif += 1
        bit >>=1 
        fedor >>=1
        
    return dif  


frinds = 0
for i in range(len(arr)-1):
    if findbit(arr[i],arr[m]) <= k:
        frinds += 1

print(frinds)



