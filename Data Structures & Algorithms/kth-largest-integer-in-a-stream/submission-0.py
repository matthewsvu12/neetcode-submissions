class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = [n for n in nums]
        heapq.heapify(self.stream)
        self.k = k
        print(self.stream, k)
        # [1, 2, 3, 3] 3

    def add(self, val: int) -> int:
        # [1, 2, 3, 3, 3] val = 3, k = 3
        heapq.heappush(self.stream, val)
        old = []
        for i in range(len(self.stream)-self.k):
            old.append(heapq.heappop(self.stream))
            # print(temp)
        res = self.stream[0]
        # add elements back
        print(old, "old")
        for n in old:
            heapq.heappush(self.stream, n)
        print(self.stream, "stream")
        return res
