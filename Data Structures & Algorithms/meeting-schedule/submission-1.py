"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda Interval:Interval.start)
        for j in range(len(intervals)-1):
            if(intervals[j+1].start<intervals[j].end<=intervals[j+1].end):
                return False
            if(intervals[j].start<=intervals[j+1].end<=intervals[j].end or intervals[j].start<=intervals[j+1].end<=intervals[j].end):
                return False

        return True

