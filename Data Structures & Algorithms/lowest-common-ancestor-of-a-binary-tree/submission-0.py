# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        find a path from root to p and a path from root to q
        p = LL
        r = LR
        intersection of these is L 
        """
         # Helper: Iterative DFS to find the path string for a specific target (startValue or destValue)
        def getPathIterative(target):
            stack = [(root, "")]
            while stack:
                node, path = stack.pop()
                
                if node.val == target.val:
                    return path
                
                if node.left:
                    stack.append((node.left, path + "L"))
                if node.right:
                    stack.append((node.right, path + "R"))
            return ""

        pPath = getPathIterative(p)
        qPath = getPathIterative(q)
        i = 0
        while i < min(len(pPath), len(qPath)) and pPath[i] == qPath[i]:
            i += 1
        
        currS = qPath[:i]
        print(currS)
        for c in currS:
            if c == 'L':
                root = root.left
            elif c == 'R':
                root = root.right
        return root

        