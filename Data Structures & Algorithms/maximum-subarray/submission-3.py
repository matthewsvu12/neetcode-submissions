class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        runningSum = 0
        maxSum = nums[0]

        for num in nums:
            print(runningSum)
            if runningSum + num < 0:
                maxSum = max(num, maxSum)
                runningSum = 0
            else:
                runningSum += num
                maxSum = max(runningSum, maxSum)
        return maxSum