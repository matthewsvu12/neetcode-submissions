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
        p1, p2 = p, q

        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        
        return p1
        # pSeen = set()

        # while p:
        #     pSeen.add(p)
        #     p = p.parent
        
        # while q:
        #     if q in pSeen:
        #         return q
        #     q = q.parent
        # return q