class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq = 0
        res = 0
        
        left = 0
        m = {}
        for right in range(len(s)):
            m[s[right]] = m.get(s[right], 0) + 1
            if m[s[right]] > most_freq:
                most_freq = m[s[right]]
            while (right - left + 1) - most_freq > k:
                m[s[left]] -= 1
                left += 1
                
            res = max(res, right-left+1)
            
        return res

    # {'a':5, 'b':5,  'c':1}