class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. sort then get kth element
        mp = {}

        for num in nums:
            if num in mp:
                mp[num] = mp[num] + 1
            else:
                mp[num] = 1

        # instead of below, we make it min-heap instead of size k, so that at the end of constructing the heap, all that's left is the kth most frequent element!
        # heap = [(key, -v) for key, v in mp.items()]
        # heapq.heapify(heap)
        
        heap = []
        for key in mp.keys():
            heapq.heappush(heap, (mp[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
    
        return [heapq.heappop(heap)[1] for i in range(k)]

        # return [key for key, v in heapq.nsmallest(k, heap, key=lambda x: x[1])]
        