# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def good_nodes_with_max(root, cur_max):
            if not root:
                return 0
            
            cur_good_node = 1 if root.val >= cur_max else 0
            cur_max = max(cur_max, root.val)
            return cur_good_node + good_nodes_with_max(root.left, cur_max) + good_nodes_with_max(root.right, cur_max)
        
        return good_nodes_with_max(root, -101)        
