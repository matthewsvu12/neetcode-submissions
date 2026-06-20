class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(currSum, currList, index):
            if index >= len(nums) or currSum > target:
                return
            if currSum == target:
                res.append(currList[:])
                return
            

            for i in range(index, len(nums)):
                currList.append(nums[i])
                backtrack(currSum + nums[i], currList, i)
                currList.pop()
        backtrack(0, [], 0)
        return res

        