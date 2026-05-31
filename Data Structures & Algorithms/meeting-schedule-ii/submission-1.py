"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        end_times = []
        for interval in intervals:
            start, end = interval.start, interval.end
            found = False
            for i, end_time in enumerate(end_times):
                if start >= end_time:
                    end_times[i] = end
                    found = True
                    break
            if not found:
                end_times.append(end)
        return len(end_times)
            
