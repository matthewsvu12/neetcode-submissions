# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # leaf node == a valid BST
        # a null node == not a valid BST
        # Valid BST = node.left < node.val < node.right otherwise this a invalid BST return False

  
        prevNum = -1001
        def dfs(node):
            nonlocal prevNum
            if not node:
                return True           
            left = dfs(node.left)
            if prevNum >= node.val:
                return False
            prevNum = node.val
            right = dfs(node.right)
            return left and right 

        return dfs(root)
        
            

        