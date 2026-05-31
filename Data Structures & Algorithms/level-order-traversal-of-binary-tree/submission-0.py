# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [[root]]
        res = []
        while stack:
            cur_level = stack.pop()
            vals = []
            next_level = []
            for node in cur_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(vals)
            if len(next_level) > 0:
                stack.append(next_level)
        return res