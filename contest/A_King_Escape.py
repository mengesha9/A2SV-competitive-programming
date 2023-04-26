n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
visited = set()



if (ax-bx)*(ax-cx)>0 and (ay-by)*(ay-cy)>0:
    print("YES")
else:
    print("NO")    
