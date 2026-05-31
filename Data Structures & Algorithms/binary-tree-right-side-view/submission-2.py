# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        next_level = deque([[root]])

        while next_level:
            cur_level = next_level.popleft()
            res.append(cur_level[0].val)
            to_store = []
            for node in cur_level:
                if node.right:
                    to_store.append(node.right)
                if node.left:
                    to_store.append(node.left)
            if len(to_store) > 0:
                next_level.append(to_store)
        return res

