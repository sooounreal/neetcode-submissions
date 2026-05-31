class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}
        for c in s:
            if c not in letter_count:
                letter_count[c] = 1
            else:
                letter_count[c] += 1
        
        for c in t:
            if c not in letter_count:
                return False
            else:
                letter_count[c] -= 1
        
        for k in letter_count:
            if letter_count[k] != 0:
                return False
        return True