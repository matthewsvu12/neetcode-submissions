class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. sort then get kth element
        mp = {}

        for num in nums:
            if num in mp:
                mp[num] = mp[num] + 1
            else:
                mp[num] = 1

        heap = [(key, -v) for key, v in mp.items()]
        heapq.heapify(heap)

        return [key for key, v in heapq.nsmallest(k, heap, key=lambda x: x[1])]
        