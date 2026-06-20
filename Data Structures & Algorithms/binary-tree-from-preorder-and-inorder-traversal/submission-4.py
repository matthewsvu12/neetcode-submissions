# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder = self, left, right = 1, 5, 6, 2, 3, 4
        # inorder = left, self, right = 2, 6, 5, 1, 3, 4
        # (1) using preorder
        # /
        #(2) using preorder[1] and inorder[0]; 

        def dfs(pre, inord):
            if not pre:
                return None
            node = TreeNode(pre[0])
            i = inord.index(pre[0])
            node.left = dfs(pre[1:i+1], inord[:i])
            node.right = dfs(pre[i+1:], inord[i+1:])
            
            return node
        return dfs(preorder, inorder)

        

        