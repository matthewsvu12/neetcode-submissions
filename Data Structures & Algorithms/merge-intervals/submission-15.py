class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        merged = []
        #[[1,4],[5,6]] merged = [1, 4], 
        # [[1,3],[1,5],[6,7]] merged = [[1, 3], ]
        merged.append([intervals[0][0], intervals[0][1]])
        for i in range(1, len(intervals)):
            x1, y1 = merged[-1]
            x2, y2 = intervals[i]
            # [2,3],[1,5] 2 >= 1 
            if y1 >= x2:
                merged[-1][0] = min(x1, x2)
                merged[-1][-1] = max(y1, y2)
            else:
                merged.append([x2, y2])
        # if len(intervals) % 2 == 1:
        #     n = len(intervals)
        #     if merged[-1][1] >= intervals[n-1][0]:
        #         merged[-1][0] = min(merged[-1][0], intervals[n-1][0])
        #         merged[-1][1] = max(merged[-1][1], intervals[n-1][1])
        #     else:
        #         merged.append(intervals[n-1])
        return merged


        