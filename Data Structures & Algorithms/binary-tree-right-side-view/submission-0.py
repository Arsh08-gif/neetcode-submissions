# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None : return []
        dq = deque()
        dq.append(root)
        ans = [(root.val)]
        while(dq):
            level = []
            for i in range(len(dq)):
                if dq[i].left : level.append(dq[i].left)
                if dq[i].right : level.append(dq[i].right)
            if level : ans.append(level[len(level)-1].val)
            dq = deque()
            for node in level:
                dq.append(node)

        return ans 
            







        
        