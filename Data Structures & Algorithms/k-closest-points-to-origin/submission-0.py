class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maintain a min heap of size k
        # insert each point's distance into heap from (0,0) using 
        # algo sqrt((x1 - x2)^2 + (y1 - y2)^2)
        # pop k times
        res = [(math.sqrt((0-points[i][0])**2 + (0-points[i][1])**2), points[i]) for i in range(k)]
        heapq.heapify(res)
        # [[0,2],[2,2]] 0 - 0 ** 2 = 0 + (0 - 2) ^ 2 = 4 sqrt(4) = 2 
        for point in points[k:]:
            calc = math.sqrt((0-point[0])**2 + (0-point[1])**2)
            heapq.heappush(res, (calc,point))
        closest = heapq.nsmallest(k, res, key=lambda x: x[0])
        return [p[1] for p in closest]
