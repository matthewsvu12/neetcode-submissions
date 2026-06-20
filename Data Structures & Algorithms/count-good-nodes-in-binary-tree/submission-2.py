# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, maxVal):
            if not node:
                return 0
            is_good = 1 if node.val >= maxVal else 0

            left = dfs(node.left, max(node.val, maxVal))
            right = dfs(node.right, max(node.val, maxVal))

            return left + right + is_good
        return dfs(root, root.val)

        # 3
        #3 
      # 4 3

        