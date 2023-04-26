from collections import defaultdict
from collections import deque
test = int(input())

for _ in range(test):
    n = int(input())
    arr = input()
    q = deque()
    
    temp = deque()
    for i in range(2,len(arr)):
        q.append(arr[i])
    
    visit = defaultdict(int)
    visit[0] = q
    temp = deque()
    for i in range(len(arr)-1) :
        
        newtext = temp + q
        
        if q:
            q.popleft() 
        temp .append(arr[i])
        if newtext not in visit.values():
            visit[i] = newtext
    print(len(visit))    
