# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def delete(root, val) -> bool:
            if not root:
                return True
            if not root.left and not root.right and root.val == val:
                return True
            
            l = delete(root.left, val)
            r = delete(root.right, val)
            if l:
                root.left = None
            if r: 
                root.right = None
            return l and r and root.val == val
        
        if not delete(root, target):
            return root
        return None

        
