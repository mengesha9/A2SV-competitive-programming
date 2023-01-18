class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    

        i=0
        j=0
        arr=[]
        size=0
      
        while j<len(s):
            size=max(size,len(arr))
            if s[j] in arr:
                k=0
                h=arr.index(s[j])
                while k<=h:
                    arr.pop()
                    k+=1
                arr.append(s[j])     
                i+=k
            arr.append(s[j]
            j+=1  
                
        return size   
