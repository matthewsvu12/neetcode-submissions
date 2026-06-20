# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        globalMax = -math.inf
        def dfs(node):
            nonlocal globalMax
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            localSum = max(left, right) + node.val
            globalMax = max(globalMax, left + right + node.val)
            return localSum
        dfs(root)
        return globalMax