class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_l, new_r = newInterval[0], newInterval[1]
        for l, r in intervals:
            if r < new_l:
                res.append([l,r])
            elif l > new_r:
                res.append([new_l, new_r])
                new_l = l
                new_r = r
            else:
                new_l = min(l, new_l)
                new_r = max(r, new_r)
        res.append([new_l, new_r])
        return res