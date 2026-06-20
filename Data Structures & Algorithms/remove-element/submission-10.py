class Solution:        
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            # if nums[l] == val and nums[l] != nums[r] we swap and then increment l+1
            # nums = [1,1,2,3,4] val = 1
            # nums=[0,1,2,2,3,0,4,2] val = 2
            # remove
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l
            
                
        