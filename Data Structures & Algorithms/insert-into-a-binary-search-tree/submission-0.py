# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def inject(root, val):
            if root.val > val:
                if root.left:
                    inject(root.left, val)
                else:
                    node = TreeNode(val)
                    root.left = node
            else:
                if root.right:
                    inject(root.right, val)
                else:
                    node = TreeNode(val)
                    root.right = node
        inject(root, val)
        return root