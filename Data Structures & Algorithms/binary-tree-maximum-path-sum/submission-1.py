# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1000

        self.max_open_path = {None: 0}

        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root in self.max_open_path:
            return self.max_open_path[root]
        
        if root.left not in self.max_open_path:
            left = self.dfs(root.left)
        else:
            left = self.max_open_path[root.left]
        if root.right not in self.max_open_path:
            right = self.dfs(root.right)
        else:
            right = self.max_open_path[root.right]
        

        self.res = max(self.res, root.val + max(left,0) + max(right, 0))
        max_open = root.val + max(left, right, 0)
        self.max_open_path[root] = max_open
        return max_open