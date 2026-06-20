class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a heap (min?) of size k
        # heap = [2] 2
        # heap = [2, 3] 3
        # heap = [2, 3] 1
        # add 5 then pop 2 
        # heap = [2, 5] 5

        res = [n for n in nums[:k]]
        heapq.heapify(res)

        for i in range(k, len(nums)):
            heapq.heappush(res, nums[i])
            element = heapq.heappop(res)
            print(element)
        return res[0]