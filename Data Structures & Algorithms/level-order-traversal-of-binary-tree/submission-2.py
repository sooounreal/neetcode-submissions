# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [[root]]
        res = []
        i = 0
        while i < len(q):
            cur_level = q[i]
            nodes = []
            vals = []
            for node in cur_level:
                vals.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                q.append(nodes)
            if vals:
                res.append(vals)
            i += 1
        
        return res
                
        