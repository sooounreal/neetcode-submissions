class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        print(intervals)
        last_end = -50000
        res = 0
        for interval in intervals:
            next_start, next_end = interval[0], interval[1]
            if last_end > next_start:
                print(last_end, next_start, res)
                last_end = min(last_end, next_end)
                res += 1
                continue
            last_end = next_end
        return res
