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
        good = 0
        def dfs(node, v):
            nonlocal good
            if not node:
                return 0
            if node.val >= v:
                good += 1
            print(good)
            left = dfs(node.left, max(node.val, v))
            right = dfs(node.right, max(node.val, v))
        dfs(root, -101)
        return good

        # 3
        #3 
      # 4 3

        