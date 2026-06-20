# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
    #     # current_node: parent_node
    #     parent = {root: None}

    #     stk = [root]
    #     # find BOTH p and q
    #     while p not in parent or q not in parent:
    #         node = stk.pop()
            
    #         if node.left:
    #             parent[node.left] = node
    #             stk.append(node.left)
    #         if node.right:
    #             parent[node.right] = node
    #             stk.append(node.right)
                
    #     # Trace p's path upwards to the root
    #     ancestors = set()
    #     while p:
    #         ancestors.add(p)
    #         p = parent[p]
            
    #     # The first overlap is the LCA.
    #     while q not in ancestors:
    #         q = parent[q]
            
    #     return q
class Solution:
    def getPath(self, node, target, path) -> bool:
            if not node:
                return False
            if node.val == target.val:
                return True

            # Try left subtree
            path.append("L")
            if self.getPath(node.left, target, path):
                return True
            path.pop()  # Remove last character

            # Try right subtree
            path.append("R")
            if self.getPath(node.right, target, path):
                return True
            path.pop()  # Remove last character

            return False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        find a path from root to p and a path from root to q
        p = LL
        r = LR
        intersection of these is L 
        """
        
        #  # Helper: Iterative DFS to find the path string for a specific target (startValue or destValue)
        # def getPathIterative(target, p):
        #     stk = [(root, p)]
        #     while stk:
        #         node, path = stk.pop()
                
        #         if node.val == target.val:
        #             return ''.join(path)
                
        #         if node.left:
        #             path.append("L")
        #             stk.append((node.left, path))
        #             path.pop()
        #         if node.right:
        #             path.append("R")
        #             stk.append((node.right, path))
        #             path.pop()

        #     return ''

        pPath = []
        self.getPath(root, p, pPath)
        # getPathIterative(p, pPath)
        qPath = []
        self.getPath(root, q, qPath)
        # getPathIterative(q, pPath)
     
        i = 0
        while i < min(len(pPath), len(qPath)) and pPath[i] == qPath[i]:
            i += 1
        
        currS = ''.join(qPath)[:i]
        for c in currS:
            if c == 'L':
                root = root.left
            elif c == 'R':
                root = root.right
        return root

        