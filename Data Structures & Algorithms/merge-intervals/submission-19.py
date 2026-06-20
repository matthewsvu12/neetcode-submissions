class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        merged = []
        #[[1,4],[5,6]] merged = [1, 4], 
        # [[1,3],[1,5],[6,7]] merged = [[1, 3], ]
        # merged.append([intervals[0][0], intervals[0][1]])
        for i in range(len(intervals)):
            # x1, y1 = merged[-1]
            x, y = intervals[i]
            if merged and merged[-1][-1] >= x:
                merged[-1][0] = min(merged[-1][0], x)
                merged[-1][-1] = max(merged[-1][-1], y)
            else:
                merged.append([x, y])
        return merged


        