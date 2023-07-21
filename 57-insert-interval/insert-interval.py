class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # when newInterval is in front of current interval, append newI and add the res of the intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # when newInterval is behind current interval, append current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # when overlapping, merge and update newInterval 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)
        return res

