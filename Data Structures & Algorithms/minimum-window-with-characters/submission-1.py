class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counts = {}

        for c in t:
            counts[c] = counts.get(c, 0) + 1
        matches = 0
        n = len(counts.keys())

        res = ""
        left = 0
        cur = {}
        res_len = len(s)+1
        for right in range(len(s)):
            c = s[right]
            cur[c] = cur.get(c, 0) + 1
            if cur[c] == counts.get(c,0):
                matches += 1
            
            while matches == n:
                print("found candidate", s[left:right+1])
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = s[left:right+1]
                c = s[left]
                cur[c] -= 1
                left += 1
                print("shifted", c, cur[c], counts.get(c,0))
                if c in counts and cur[c] < counts[c]:
                    matches -= 1
        if res_len > len(s):
            return ""
        else:
            return res
