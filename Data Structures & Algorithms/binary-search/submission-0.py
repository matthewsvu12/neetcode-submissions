class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # mid = (hi + lo) // 2 
        # [-1,0,2,4,6,8] target = 4
        # mid = 0 + 6 / 2 = 3
        # if nums[mid] == target: return mid
        # otherwise if nums[mid] < target : check right half of array
        # if nums[mid] > target: check left half of array
        # continue until left pointer reach right pointer

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1