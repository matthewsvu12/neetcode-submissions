# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = -math.inf
        def rec(node):
            nonlocal diff
            if not node:
                return 0
            left = rec(node.left) # 1
            right = rec(node.right) # 2
            # 2 - 1 = 1 1 - 2 = -1
            diff = max(diff, abs(right-left))

            return max(left, right) + 1
        rec(root)
        return False if diff > 1 else True
        