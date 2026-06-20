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
            stk = [(root, [])]
            while stk:
                node, path = stk.pop()
                
                if node.val == target.val:
                    return ''.join(path)
                
                if node.left:
                    path.append("L")
                    stk.append((node.left, path[:]))
                    path.pop()
                if node.right:
                    path.append("R")
                    stk.append((node.right, path[:]))
                    path.pop()

            return ''

        pPath = getPathIterative(p)
        qPath = getPathIterative(q)
        print(qPath)
        print(pPath)
     
        i = 0
        while i < min(len(pPath), len(qPath)) and pPath[i] == qPath[i]:
            i += 1
        currS = qPath[:i]
        for c in currS:
            if c == 'L':
                root = root.left
            elif c == 'R':
                root = root.right
        return root

        