class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        1. keep inserting deque, unless we encounter a element that's larger than leftmost element in deque i.e root. 
        2. Then we pop the leftmost element, and insert larger new element on t
        """

        window = deque()

        l, r = 0, 0

        while r < k:
            if window and window[0] < nums[r]:
                window.popleft()
                window.appendleft(nums[r])
            else:
                window.append(nums[r])
            print(r)
            r += 1
        print(window, r)
        res = []
        res.append(window[0])
        for r in range(r, len(nums)):
            print("first", window)

            if window[0] == nums[l]:
                window.popleft()
            l += 1
            print("2nd", window, nums[r])

            while window and nums[r] > window[-1] :
                window.pop()

            window.append(nums[r])
            res.append(window[0])

        return res