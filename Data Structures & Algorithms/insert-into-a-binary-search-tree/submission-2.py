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
            # if not node:
            #     return
            if not node.left and node.val > val:
                node.left = TreeNode(val)
                return
            if not node.right and node.val < val:
                node.right = TreeNode(val)
                return
            # val = 6
            if node.val < val:
                if node.right:
                    dfs(node.right)
            
            if node.val > val:
                if node.left:
                    dfs(node.left)
        dfs(root)
        return root

        