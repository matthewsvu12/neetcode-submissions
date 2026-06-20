# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)

        def dfs(node):
            if not node:
                return

            if node.val < val:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)

            if node.val > val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)
        dfs(root)
        return root

        