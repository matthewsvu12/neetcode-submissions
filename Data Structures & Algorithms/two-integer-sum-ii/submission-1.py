class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        ## [1,2,3,4] target = 6
        # 1 + 2 = 3
        # 
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            elif total > target:
                r -= 1
        return [l+1, r+1]
            
            
        