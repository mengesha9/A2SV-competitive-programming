from collections import defaultdict
from collections import deque
n = int(input())
s = input()
freq = defaultdict(int)
q = deque()
j = 0
while j<len(s):
    q.append(s[j])
    if len(q)== 2:
        freq[''.join(q)]+=1
        q.popleft()

    j+= 1    

print(max(freq , key=freq.get))

