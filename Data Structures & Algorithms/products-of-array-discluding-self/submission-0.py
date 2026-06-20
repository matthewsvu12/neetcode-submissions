class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum
        # 
        prefixSum = [0 for n in nums]
        rightPrefixSum = [0 for n in nums]
        rightPrefixSum[-1] = nums[-1]
        prefixSum[0] = nums[0]
        print(nums)
        # multiply prefixSum[i] by prefixSum[i-1]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] * nums[i]
        print(prefixSum)
        for i in range(len(nums)-2, -1, -1):
            rightPrefixSum[i] = rightPrefixSum[i+1] * nums[i]
        print(rightPrefixSum)
        # nums=[1,2,4,6]
        # prefixSum = [1, 2, 8, 48]
        # i = 2
        # prefixSum[i-1] * prefixSum[i+1]
        # Output: [48,24,12,8]
        # i = 0 output[i] = rightPrefix[i+1] 
        # i = 1 output[i] = leftPrefix[i-1] * rightPrefix[i+1] 
        # i = 2 output[i] = leftPrefix[i-1] * rightPrefix[i+1]
        # i = 3 output[i] = leftPrefix[i-1]
        
        output = [0 for n in nums]
        output[0] = rightPrefixSum[1]
        for i in range(1, len(nums)-1):
            output[i] = prefixSum[i-1] * rightPrefixSum[i+1]
        output[-1] = prefixSum[len(nums)-2]

        

        return output
        
        