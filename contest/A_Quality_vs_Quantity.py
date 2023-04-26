test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    i = 1
    j = len(arr)-1
    count_red = 0
    count_blue = 1 
    sum_blue = arr[0]
    sum_red = 0
    while i<j:
        sum_red += arr[j]
        sum_blue += arr[i]
        i += 1
        j -= 1
        
    if sum_blue < sum_red :
        print("YES")
    else:
        print("NO")    

            

