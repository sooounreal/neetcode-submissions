class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}
        for c in s1:
            counts[c] = counts.get(c, 0) + 1
        
        cur_counts = {}
        start = 0
        for i,c in enumerate(s2):
            if c not in counts:
                cur_counts = {}
                start = i+1
                continue
            cur_counts[c] = cur_counts.get(c,0) + 1

            while cur_counts[c] > counts[c]:
                cur_counts[s2[start]] -= 1
                start += 1

            if i - start + 1 == len(s1):
                return True
        
        return False