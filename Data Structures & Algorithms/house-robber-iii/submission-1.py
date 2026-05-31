# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        # robbed = parent robbed
        def dfs(root, robbed):
            if (root, robbed) in cache:
                return cache[(root, robbed)]
            if not root:
                return 0
            if not root.left and not root.right:
                if not robbed:
                    return root.val
                return 0
            
            if robbed:
                res = dfs(root.left, False) + dfs(root.right, False)
            else:
            # either rob current or dont
                res = max(root.val + dfs(root.left, True) + dfs(root.right, True), dfs(root.left, False) + dfs(root.right, False))
            cache[(root, robbed)] = res
            return res
        
        return dfs(root, False)
