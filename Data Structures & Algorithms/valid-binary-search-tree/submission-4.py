# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def is_valid(root, upper, lower):
            if not root:
                return True
            
            if root.val >= upper or root.val <= lower:
                return False
            
            return is_valid(root.left, root.val, lower) and is_valid(root.right, upper, root.val)
        
        return is_valid(root, 1001, -1001)