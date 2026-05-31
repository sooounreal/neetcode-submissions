# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        
        left_is_sub = self.isSubtree(root.left, subRoot)
        right_is_sub = self.isSubtree(root.right, subRoot)
        return self.is_same(root, subRoot) or left_is_sub or right_is_sub

    def is_same(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        return root.val == subRoot.val and self.is_same(root.left, subRoot.left) and self.is_same(root.right, subRoot.right)