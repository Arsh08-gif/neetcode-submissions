# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None : return 0
        count = 1
        q = deque([(root,root.val)])
        while q:
            parent, max_val = q.popleft()
            # print(parent.val , max_val)
            if parent.left: 
                q.append((parent.left, max(parent.left.val,max_val)))
                # print(parent.left.val, max(parent.left.val,max_val))
                if parent.left.val >= max_val: count += 1
            if parent.right : 
                q.append((parent.right, max(parent.right.val,max_val)))
                # print(parent.right.val, max(parent.right.val,max_val))
                if parent.right.val >= max_val: count += 1
            # print(count)
        return count


# 3
# /
# 3
# /\
# 4 2
        