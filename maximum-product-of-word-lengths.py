class Solution:
    def maxProduct(self, words: List[str]) -> int:

        def bitmask(word):
            mask = 0

            for c in word:
                mask |= 1<< ord(c)-ord('a')
            return mask 

        arr = []
        ans = 0
        for word in words:
            arr.append(bitmask(word))
        print(arr)
        
        for i in range(len(words)):
            for j in range(i):
                if not (arr[i] & arr[j]):
                    ans = max(ans,len(words[i])*len(words[j]))

        return ans