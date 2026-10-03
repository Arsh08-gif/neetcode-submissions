"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        return self.dfs(node,old_to_new)
    
    def dfs(self,n,old_to_new):
        if n in old_to_new:
            return old_to_new[n]
        
        clone = Node(n.val)
        old_to_new[n] = clone

        for neighbor in n.neighbors:
            clone.neighbors.append(self.dfs(neighbor,old_to_new))
        return clone