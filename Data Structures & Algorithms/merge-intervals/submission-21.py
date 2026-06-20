class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        merged = []
        #[[1,4],[5,6]] merged = [1, 4], 
        # [[1,3],[1,5],[6,7]] merged = [[1, 3], ]
        for interval in intervals:
            # x1, y1 = merged[-1]
            x, y = interval
            if merged and merged[-1][-1] >= x:
                merged[-1][-1] = max(merged[-1][-1], y)
            else:
                merged.append(interval)
        return merged


        