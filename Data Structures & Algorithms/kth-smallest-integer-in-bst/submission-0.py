# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        in order traversal
        if not node:
            return
        
        dfs(node.left)
        k -= 1
        if k == 0:
            return node.val
        dfs(node.right)
        """
        smallest = 1001
        currK = k
        def dfs(node):
            nonlocal currK
            nonlocal smallest
            if not node:
                return
            
            left = dfs(node.left)
            currK -= 1
            if currK == 0:
               print('a: ', node.val)
               smallest = node.val
               return
            right = dfs(node.right)

            return

             
        dfs(root)
        return smallest
