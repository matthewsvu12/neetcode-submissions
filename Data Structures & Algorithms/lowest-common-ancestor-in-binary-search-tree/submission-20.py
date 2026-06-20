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
        if p.val > q.val:
            temp = p.val
            p.val = q.val
            q.val = temp

        def dfs(node, p, q):
            if p.val <= node.val and node.val <= q.val:
                return node
            elif p.val < node.val and node.val > q.val:
                return dfs(node.left, p, q)
            else:
                return dfs(node.right, p, q)
        return dfs(root, p , q )
        # return dfs(root, p if p.val < q.val else q, q if p.val < q.val else p)
