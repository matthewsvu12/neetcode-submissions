class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(Counter(nums)) != len(nums)
        