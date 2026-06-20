# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find LCA using BST properties
        left subtree <= curr <= right subtree == LCA

        if p.val <= curr and curr <= q.val:
            return curr
        elif p.val < curr and curr > q.val:
            return dfs(curr.left)
        else:
            return dfs(curr.right)

        """
        def dfs(node, p, q):
            # p = 3 , q = 5 root = 2
            if p.val <= node.val and node.val <= q.val:
                return node
            # if 3 < 2 and 2 > 5
            elif p.val < node.val and node.val > q.val:
                return dfs(node.left, p, q)
            # if 3 > 2 and 2 < 5
            else:
                return dfs(node.right, p, q)
        
        return dfs(root, p if p.val < q.val else q, q if p.val < q.val else p)
