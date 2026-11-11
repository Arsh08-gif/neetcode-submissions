# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_count = 0
        ans = 0
        def in_order(node):
            nonlocal node_count, ans
            if node is None : return None
            left = in_order(node.left)
            node_count += 1
            if node_count == k:
                ans =  node.val
            right = in_order(node.right)
            return ans


        return in_order(root)



        

