# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def isValidTree(node,low, high):
            if node is None: return True
            if not (low < node.val < high): return False
            left = isValidTree(node.left,low,node.val)
            right = isValidTree(node.right,node.val, high)

            return left and right
            
        return isValidTree(root, float('-inf'), float('inf'))
        

#   5
# /    \
# 4     6
#        /\
#        3 7
        