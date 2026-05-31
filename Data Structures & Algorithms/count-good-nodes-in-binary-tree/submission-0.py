# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(node, cur_max):
            if not node:
                return
            if node.val >= cur_max:
                res.append(node)
                cur_max = node.val
                print(node.val)
            if node.left:
                dfs(node.left, cur_max)
            if node.right:
                dfs(node.right, cur_max)

        if not root:
            return 0

        dfs(root, -1000)
        return len(res)
        
