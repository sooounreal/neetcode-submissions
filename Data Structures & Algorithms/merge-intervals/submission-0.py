class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals)
        res = []
        cur_l, cur_r = intervals[0]
        for next_l, next_r in intervals[1:]:
            if cur_r >= next_l:  # intersect
                cur_l = min(cur_l, next_l)
                cur_r = max(cur_r, next_r)
            else:
                res.append([cur_l,cur_r])
                cur_l = next_l
                cur_r = next_r
        res.append([cur_l, cur_r])
        return res

