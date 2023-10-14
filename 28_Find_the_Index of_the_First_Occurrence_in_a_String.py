class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        prime = 31
        modulus = 10**9 + 7

        n = len(haystack)
        m = len(needle)

        needle_hash = 0
        curr_hash = 0
        power = 1

        for i in range(m):
            needle_hash = (needle_hash * prime + ord(needle[i])) % modulus
            curr_hash = (curr_hash * prime + ord(haystack[i])) % modulus
            power = (power * prime) % modulus

        for i in range(n - m + 1):
            if curr_hash == needle_hash and haystack[i:i+m] == needle:
                return i

            if i + m < n:
                curr_hash = (curr_hash * prime - ord(haystack[i]) * power + ord(haystack[i + m])) % modulus

        return -1
