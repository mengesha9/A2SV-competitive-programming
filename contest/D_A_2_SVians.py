from collections import Counter
n=int(input())
s=input().split()
arr=[]

for i in range(n):
    dic=Counter(s[i])
    arr.append([s[i],dic])
bad = set(input().split())
num_excellent=0
for name, dic in arr:
    if name not in bad and len(set(dic.values()))==1:
        num_excellent+=1
print(num_excellent)    

