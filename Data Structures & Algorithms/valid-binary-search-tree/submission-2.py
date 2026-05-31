# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_valid = self.isValidInRange(root.left, -1000, root.val) if root.left else True
        right_valid = self.isValidInRange(root.right, root.val, 1000) if root.right else True
        return left_valid and right_valid

    def isValidInRange(self, root, lower, upper):
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        # if root.left and root.val <= lower:
        #     return False
        # if root.right and root.val >= upper:
        #     return False
        left_valid = self.isValidInRange(root.left, lower, root.val) if root.left else True
        right_valid = self.isValidInRange(root.right, root.val, upper) if root.right else True
        return left_valid and right_valid