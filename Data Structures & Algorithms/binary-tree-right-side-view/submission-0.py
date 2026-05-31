# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append([root])
        while q:
            cur_level = q.popleft()
            added = False
            next_level = []
            for node in cur_level:
                if node:
                    if not added:
                        res.append(node.val)
                        added = True
                    next_level.append(node.right)
                    next_level.append(node.left)
            if next_level:
                q.append(next_level)
        return res
            
