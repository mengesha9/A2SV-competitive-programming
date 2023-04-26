from collections import defaultdict
n = int(input())

sup = defaultdict(list)
for i in range(n):
    pi = int(input())
    sup[i+1].append(pi)
    if pi != -1:
        sup[i+1]=  sup[i+1] + sup[pi]
    
maxlevel = 0
for k,v in sup.items():
    maxlevel = max(maxlevel,len(v))

print(maxlevel)   


