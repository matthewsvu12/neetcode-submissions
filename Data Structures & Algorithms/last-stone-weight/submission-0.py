class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxheap(stones) = [-2,-2,-3,-4,-6]
        # pop -6 and -4 out and negate them to be 6, 4
        # if 4 < 6 : destroy 4 put 6-4=2 back
        # [-2,-2,-2,-3,]
        # pop -3 and -2 out negate them to 3, 2
        # 2 < 3 so smash them 3-2 = 1 and add that back
        # [-1, -2,-2]
        # pop -2,-2 negate them 2,2
        # 2 == 2, don't do anything since you've already popped them
        # since len(stones) == 1: return stones[0]
        res = []
        for stone in stones:
            heapq.heappush(res,-stone)
        
        while len(res) > 1:
            y = -heapq.heappop(res)
            x = -heapq.heappop(res)
            sub = y - x
            print(x, y)
            if x < y:
                heapq.heappush(res, -sub)
            elif x == y:
                continue
                # heapq.heappush(res, -x)
                # heapq.heappush(res, -y)
            print(res)


        return 0 if len(res) == 0 else -res[0]