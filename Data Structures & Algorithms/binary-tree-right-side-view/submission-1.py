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
        dq = deque([root])
        # dq.append(root)
        ans = []
        while(dq):
            ans.append(dq[-1].val)
            n = len(dq)
            for  _ in range(n):
                node = dq.popleft()
                if node.left : dq.append(node.left)
                if node.right : dq.append(node.right)

        return ans 
            







        
        