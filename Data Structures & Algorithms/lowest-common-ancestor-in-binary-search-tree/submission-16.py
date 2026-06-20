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
        elif p.val <= curr and curr > q.val:
            return dfs(curr.left)
        else:
            return dfs(curr.right)

        """
        # 1. find p and q using dfs
        def findNode(node, p, q):
            # p = 3 , q = 5 root = 2
            print(node.val, p.val, q.val)
            if node and p.val <= node.val and node.val <= q.val:
                print("curr", node.val)
                return node
            # if 3 < 2 and 2 > 5
            elif node.left and p.val < node.val and node.val > q.val:
                print("LEFT", node.val, node.left.val)
                return findNode(node.left, p, q)
            # if 3 > 2 and 2 < 5
            elif node.right and p.val > node.val and node.val < q.val:
                print("RIGHT", node.val, node.right.val)
                return findNode(node.right, p, q)
            return node
        return findNode(root, p if p.val < q.val else q, q if p.val < q.val else p)
