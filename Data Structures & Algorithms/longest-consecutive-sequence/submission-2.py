class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elements = set(nums)
        longest = 1
        for n in nums:
            running = 1
            # finds out if the current num is the start of a sequence of elements
            if n-1 not in elements:
                # Keep counting the running length of the sequence of elements as long as we can
                while n+running in elements:
                    running += 1
            longest = max(longest, running)

        return longest