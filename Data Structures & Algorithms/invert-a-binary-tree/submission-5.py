# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # do right first then left
        # swap right with left and swap left with right
        def dfs(node):
            if not node:
                return None
            # detecting if we reach a leaf
            # if not node.left and not node.right:
            #     return 0
            # if not node.left:
            #     node.left = node.right
            #     node.right = None
            #     dfs(node.left)
            #     return 0
            # elif not node.right:
            #     node.right = node.left
            #     node.left = None
            #     dfs(node.right)
            #     return 0
    
            # dfs(node.right)
            # swap
            temp = dfs(node.right)
            node.right = dfs(node.left)
            node.left = temp

            # dfs(node.right)
            return node

        # root = 1
        dfs(root)
        return root
        