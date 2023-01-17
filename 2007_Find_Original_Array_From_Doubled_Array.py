class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        if len(changed)%2!=0:
            return []
        count=Counter(changed)
        print(count)
        # {1: 1, 3: 1, 4: 1, 2: 1, 6: 1, 8: 1}
        # [1,3,4,2,6,8]
        # ({6: 1, 3: 1, 0: 1, 1: 1})   [6,3,0,1]
        arr=[]
        for i in range(len(changed)):
            if changed[i] in count and count[changed[i]]>=1 :
                count[changed[i]]-=1
                if changed[i]*2 in count and count[changed[i]*2]>=1:

                    arr.append(changed[i])
                    count[2*changed[i]]-=1
              

        return  arr if len(arr)==len(changed)//2 else []    
