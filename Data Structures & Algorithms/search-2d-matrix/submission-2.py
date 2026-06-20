class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        mid = lo + (hi-lo) // 2

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        # do binary search on the rows 
        # if target[mid][0] == target: return True
        # if the target > matrix[mid][0] and target <= matrix[mid][len(matrix[0])-1]
        # then binary search columns

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if matrix[mid][0] == target:
                return True
            elif target > matrix[mid][0] and target <= matrix[mid][len(matrix[0])-1]:
                return self.binarySearch(matrix[mid], target)
            elif target > matrix[mid][len(matrix[0])-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
