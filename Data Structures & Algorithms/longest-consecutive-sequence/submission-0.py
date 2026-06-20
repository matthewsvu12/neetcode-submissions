class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elements = set()
        for n in nums:
            elements.add(n)

        longest = 1
        for n in nums:
            running = 1
            currNum = n
            while currNum+1 in elements:
                running += 1
                currNum += 1
            longest = max(longest, running)

        return longest