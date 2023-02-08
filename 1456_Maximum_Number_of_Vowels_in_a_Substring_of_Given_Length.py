class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=('a','i','o','u','e')
        res=0
        total=0
        j=0
        i=0
        while j<len(s):
            if j-i>k-1:
                if s[i] in vowels:
                    res-=1
                i+=1
            if s[j] in vowels:
                res+=1
            j+=1
            total=max(res,total)
        return total





            









       


