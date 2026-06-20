class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        1. keep inserting deque, unless we encounter a element that's larger than leftmost element in deque i.e root. 
        2. Then we pop the leftmost element, and insert larger new element on t
        """

        window = deque()

        l, r = 0, 0

        while r < k:
            while window and window[-1] < nums[r]:
                window.pop()
            window.append(nums[r])
            r += 1

        res = []
        res.append(window[0])
        for r in range(r, len(nums)):
            if window[0] == nums[l]:
                window.popleft()
            l += 1
            while window and window[-1] < nums[r]:
                window.pop()
            window.append(nums[r])
            res.append(window[0])

        return res