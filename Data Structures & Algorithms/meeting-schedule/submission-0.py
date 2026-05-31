"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        last_end = 0
        for interval in intervals:
            start = interval.start
            if start < last_end:
                return False
            last_end = interval.end
        return True