from collections import defaultdict
s = int(input())

for _ in range(s):

    num = input()

    i,res=0,len(num)+1
    hash_map=defaultdict(int)

    for j in range(len(num)):
        hash_map[num[j]]+=1
        while len(hash_map.values())==3:
            res = min(res, sum(hash_map.values()))
            hash_map[num[i]]-=1
            if hash_map[num[i]]==0:
                del hash_map[num[i]]
            i+=1

    print(res) if res <=len(num)  else print(0)    


