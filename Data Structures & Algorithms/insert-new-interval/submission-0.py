class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Catch all intervals strictly before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # Phase 2: Merge all overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # Push the fully merged interval into our result
        res.append(newInterval)
        
        # Phase 3: Catch all remaining intervals strictly after
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res