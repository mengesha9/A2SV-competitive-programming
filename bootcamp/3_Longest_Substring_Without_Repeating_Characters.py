class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    

        m = set()
        left = 0
        maxx = 0
        for right in range(len(s)):
            while s[right] in m:
                m.remove(s[left])
                left+=1
            maxx = max(maxx,len(m)+1)
            m.add(s[right])
        return maxx           



       
