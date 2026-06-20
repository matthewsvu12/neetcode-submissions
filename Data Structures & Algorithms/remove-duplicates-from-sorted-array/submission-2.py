class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        seen = set()
        # two pointers
        for r in range(1, len(nums)):
            # nums = [1,1,2,3,4]
            # nums = [2,10,10,30,30,30]
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

        return l+1

