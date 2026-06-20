"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # keep going up for p until root keep track of nodes we see
        # keep going up for q until root if we see a node from the nodes seen from the pPath return that node

        pSeen = set()

        while p:
            pSeen.add(p)
            p = p.parent
        
        while q not in pSeen:
            q = q.parent
        return q