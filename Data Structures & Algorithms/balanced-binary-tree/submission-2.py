# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def height(node):
            nonlocal bal
            if node == None : return 0
            left_height = height(node.left) 
            right_height = height(node.right) 
            if abs(left_height - right_height) > 1 : bal = False
            return max(left_height, right_height) + 1
        
        height(root)
        return bal



# [1,2,2,3,null,null,3,4,null,null,4]
# 1
# /\
# 2 2
# /  \
# 3   3
# /   \   
# 4    4


