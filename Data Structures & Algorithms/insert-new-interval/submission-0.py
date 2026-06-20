class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ## intervals = [[1,3],[2,5],[4,6]], newInterval = [2,5] merged = [[1,5], [2,6]]
        # if end position of interval 1 >= start position of interval 2 = overlapping intervals
        # how do we merge? new merged interval = start position of interval 1, end position of interval 2 = [1, 5]
        # for interval in intervals:

        # [1,3] new interval = [0,4] [2,5]
        def merge(interval1):
            newInterval[0] = min(interval1[0], newInterval[0])
            newInterval[-1] = max(interval1[-1], newInterval[-1])
        res = []
        for i in range(len(intervals)):
            # merge interval
            # [[1,3],[4,6]] newInterval = [0, 4]
            # [1,2],[3,5],[9,10]], newInterval = [6,7]
            #                                      [3,5]
            # res = [1,2], [3,5], [6,7], [9,10]
            # [[1,3],[4,6]] newInterval = [0, 4]
            # res = {0}
            if newInterval[0] > intervals[i][-1]:
                res.append(intervals[i])
            elif newInterval[-1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else: 
                merge(intervals[i])
        res.append(newInterval)

        return res