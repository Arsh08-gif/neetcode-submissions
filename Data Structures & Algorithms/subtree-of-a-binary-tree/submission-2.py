# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root,subRoot):
        if root is None and subRoot is None : return True
        if root is None : return False
        if subRoot is None : return False
        if root.val != subRoot.val : return False

        left = self.isSameTree(root.left, subRoot.left)
        right = self.isSameTree(root.right, subRoot.right)
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None : return True
        if root is None : return False
        if subRoot is None : return True

        if self.isSameTree(root,subRoot) : return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
