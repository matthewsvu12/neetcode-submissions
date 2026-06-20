class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        heapq.heapify(self.stream)
        print(self.stream)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
            print(self.stream)
        print(self.stream, "end")
        

    def add(self, val: int) -> int:
        # [1, 2, 3, 3, 3] val = 3, k = 3
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.k:
            heapq.heappop(self.stream)

        return self.stream[0]
