# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seen_none = False
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if not node:
                    seen_none = True
                elif seen_none:
                    return False
                else:
                    q.append(node.left)
                    q.append(node.right)
        return True
