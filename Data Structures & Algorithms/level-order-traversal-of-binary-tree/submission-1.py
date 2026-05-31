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
        queue = deque([root])
        res = []
        size = 1
        while queue:
            lvl_list = []
            new_size = 0
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    new_size += 1
                if node.right:
                    queue.append(node.right)
                    new_size += 1
                lvl_list.append(node.val)
            size = new_size
            res.append(lvl_list)
        return res