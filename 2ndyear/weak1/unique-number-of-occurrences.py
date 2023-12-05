class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:


       
        d={}
        for  n in arr:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        d2={}
        num=[]

        for i in range(len(arr)):
            if arr[i] not in d2:
                num.append(d[arr[i]])
                d2[arr[i]]=1
        print(num)
        num.sort()
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                return False
        return True        





             


              
                 
            
