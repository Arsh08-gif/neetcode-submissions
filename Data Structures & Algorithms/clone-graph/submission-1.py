"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        vis = {}

        def dfs(orig):
            if orig in vis: return vis[orig]

            copy = Node(orig.val)
            vis[orig] = copy

            for neigbor in orig.neighbors:
                copy.neighbors.append(dfs(neigbor))
            
            return copy
        
        return dfs(node)
        