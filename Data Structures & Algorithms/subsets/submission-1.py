class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        def dfs(combo: list, i: int):
            res.append(combo[:])
            if i >= len(nums):
                return
            # nums = [1, 2]
            # combo = [1] i == 0
            # combo = [1, 2] i == 1
            # combo = [1, 2, 3] i == 2
            # combo = [1, 2, 3] i == 3 res.append(combo)
            # combo = [1, 2] = i == 2
            # combo = [1, 2]  i == 3 res.append(combo)
            
            for index in range(i, len(nums)):
                combo.append(nums[index])
                dfs(combo, index+1)
                combo.pop()
        dfs([], 0)

        return res
        