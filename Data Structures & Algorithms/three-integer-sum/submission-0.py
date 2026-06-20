class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        triplets = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    count = nums[i] + nums[j] + nums[k]
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if count == 0 and triplet not in triplets:
                        res.append([nums[i], nums[j], nums[k]])
                        triplets.add(triplet)
        return res
        