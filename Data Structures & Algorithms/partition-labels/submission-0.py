class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        res = []
        i = 0
        cur_counts = {}
        cur_len = 0
        for i in range(len(s)):
            c = s[i]
            cur_len += 1
            # add to cur
            cur_counts[c] = cur_counts.get(c,0) + 1

            if cur_counts[c] == counts[c]:
                cur_counts.pop(c)
            
            if not cur_counts:
                res.append(cur_len)
                cur_len = 0
        return res


