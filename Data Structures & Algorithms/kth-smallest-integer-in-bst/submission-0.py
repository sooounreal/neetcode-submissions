# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = []

        def dfs(root, k):
            if not root:
                return
            if len(cur) >= k:
                return

            dfs(root.left, k)
            cur.append(root.val)
            dfs(root.right, k)

        dfs(root, k)
        return cur[k-1]
    