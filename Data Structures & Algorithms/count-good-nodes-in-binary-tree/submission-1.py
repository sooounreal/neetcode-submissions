# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + self.goodNodesWithMax(root.left, root.val) + self.goodNodesWithMax(root.right, root.val)

    
    def goodNodesWithMax(self, root, cur_max):
        if not root:
            return 0
        if root.val >= cur_max:
            return 1 + self.goodNodesWithMax(root.left, root.val) + self.goodNodesWithMax(root.right, root.val)
        else:
            return self.goodNodesWithMax(root.left, cur_max) + self.goodNodesWithMax(root.right, cur_max)


        

