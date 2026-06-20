class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            # two pointer solution
            # nums = [-1,0,1,2,-1,-4] sort it
            # nums = [-4,-1,-1,0,1,2] sorted
            # anchor on i-th index, then conduct two pointer search from (i+1, len(nums)) for j and k
            # increment left pointer if nums[i] + nums[l] + nums[r] < 0
            # decrement right pointer if nums[i] + nums[j] + nums[k] > 0
            # if nums[i] + nums[j] + nums[k] == 0: add triplet to result
            l = i+1
            r = len(nums)-1
            while l < r:
                count = nums[i] + nums[l] + nums[r]
                if count < 0:
                    l += 1
                elif count > 0:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
            # for j in range(i+1, len(nums)):
            #     for k in range(j+1, len(nums)):
            #         count = nums[i] + nums[j] + nums[k]
            #         triplet = (nums[i], nums[j], nums[k])
            #         if count == 0 and triplet not in triplets:
            #             res.append([nums[i], nums[j], nums[k]])
            #             triplets.add(triplet)
        return list(res)
        