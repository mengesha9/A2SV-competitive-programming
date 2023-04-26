n, d = map(int,input().split())
arr = list(map(int,input().split()))

no_palayers = n
arr.sort() 
count_win = 0
j = len(arr)-1
while j>=0:
    x = d//arr[j]
    if no_palayers >= (x+1):
            no_palayers -= (x+1)
            count_win += 1
    if no_palayers < (x+1):
        break    
    j-=1  

print(count_win)
