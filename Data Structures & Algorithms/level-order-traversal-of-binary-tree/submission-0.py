# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        dq = deque([root])
        ans = []
        level = 0
        

        while(dq):
            level_list = []
            val_list = []
            for i in range(len(dq)):
                level_list.append(dq.popleft())
            
            for node in level_list:
                val_list.append(node.val)
                if node.left : dq.append(node.left)
                if node.right : dq.append(node.right)
                
            ans.append(val_list)
            level += 1
        
        return ans
                
        

        