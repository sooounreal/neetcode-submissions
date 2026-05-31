class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # odd
        for i in range(len(s)):
            res += 1
            half = 1
            while i - half >= 0 and i + half < len(s) and s[i-half] == s[i+half]:
                half +=1
                res += 1
        
        # even
        for i in range(len(s)):
            half = 1
            while i - half >= 0 and i + half - 1 < len(s) and s[i-half] == s[i+half-1]:
                half += 1
                res += 1
        return res
