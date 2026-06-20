class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        print(intervals)

        overlapping = 0
        # [1, 2] = 2-1 = 1 # 1 overlapping
        # [1, 4] = 4-1 = 3 #  2 overlapping
        # [2, 4] = 4-2 = 2 # 1 overlapping
        # [1,11] , [9, 13], [10, 14] count == 1  
        # prevEnd = 2 curr = [1, 4] so overlapping + 1
        # preveEnd = 4 curr = [2 , 4] so overlapping + 1 
        # len(intervals) = 3 and 2 overlapping what is minimum number of overlapping intervals to remove? 3 - 2 = 1
        # Input: intervals = [[1,2],[1,4],[2,4]]
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < prevEnd:
                prevEnd = min(interval[1], prevEnd)
                overlapping += 1
            else:
                prevEnd = interval[1]



        return overlapping
        