# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            # max depth of left
            left = dfs(root.left)
            # max depth of right
            right = dfs(root.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter