class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. sort then get kth element
        mp = {}

        for num in nums:
            if num in mp:
                mp[num] = mp[num] + 1
            else:
                mp[num] = 1

        res = [(k, -v) for k, v in mp.items()]
        heapq.heapify(res)

        
        
        return [k for k, v in heapq.nsmallest(k, res, key=lambda x: x[1])]
        