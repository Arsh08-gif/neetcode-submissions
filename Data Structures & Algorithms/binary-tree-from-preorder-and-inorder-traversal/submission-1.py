# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_idx_map = {}
        for i,num in enumerate(inorder):
            in_idx_map[num] = i
        
        pre_idx = 0

        def build(l,r):
            nonlocal pre_idx
            if l > r : return
            root = TreeNode(preorder[pre_idx])
            mid = in_idx_map[root.val]
            pre_idx += 1
            root.left = build(l,mid-1)
            root.right = build(mid+1,r)
            return root
        return build(0,len(inorder)-1)
