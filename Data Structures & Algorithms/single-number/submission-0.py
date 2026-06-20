class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #  [7,6,6,7,8]
        #  1101 1100 XOR = 0001
        #  0001 1100 XOR = 1101
        #  1101 1101 XOR = 0000
        #  0000 1111 XOR = 1111

        runningSum = nums[0]

        for i in range(1, len(nums)):
            runningSum ^= nums[i]
        return runningSum
        