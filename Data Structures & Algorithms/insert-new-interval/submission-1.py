class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ## intervals = [[1,3],[2,5],[4,6]], newInterval = [2,5] merged = [[1,5], [2,6]]
        # if end position of interval 1 >= start position of interval 2 = overlapping intervals
        # how do we merge? new merged interval = start position of interval 1, end position of interval 2 = [1, 5]
        # for interval in intervals:

        # [1,3] new interval = [0,4] [2,5]
        def merge(interval):
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[-1] = max(interval[-1], newInterval[-1])
        res = []
        for i, curr_interval in enumerate(intervals):
            # merge interval
            # [[1,3],[4,6]] newInterval = [0, 4]
            # [1,2],[3,5],[9,10]], newInterval = [6,7]
            #                                      [3,5]
            # res = [1,2], [3,5], [6,7], [9,10]
            # [[1,3],[4,6]] newInterval = [0, 4]
            # res = {0}
            new_start, new_end = newInterval[0], newInterval[1]
            start, end = curr_interval[0], curr_interval[1]
            if new_start > end:
                res.append(curr_interval)
            elif new_end < start:
                res.append(newInterval)
                return res + intervals[i:]
            else: 
                merge(curr_interval)
        res.append(newInterval)

        return res