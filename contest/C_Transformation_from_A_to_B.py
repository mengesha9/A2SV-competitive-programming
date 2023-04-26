a,b = map(int,input().split())
result = []
result.append(b)

while b >a:
    if b % 10 == 1:
        result.append(b // 10)
        b = b // 10
    elif (b % 10 )   % 2 == 0:
        result.append(b//2) 
        b = b//2
    else:
        break



# def dfs(num,arr):
#     arr.append(num)
#     if num == a:
#         result.append(arr.copy())
#         return
#     if num>a:
#         return False  
#     dfs(num*2,arr)
#     dfs(num*10+1,arr)



# dfs(b,[])

if a != b:
    print("NO")
else:
    print("YES")
    print(len(result))
    result.reverse()
    print(* result)

    


